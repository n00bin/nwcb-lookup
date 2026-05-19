#!/usr/bin/env python3
"""Flip the PREVIEW_ACTIVE flag in js/preview-config.js, then commit + push.

Run via the double-click wrapper `flip-preview.cmd` in the website root,
or directly with `python scripts/flip-preview.py`.

Reads `js/preview-config.js`, shows the current state (ON / OFF) and the
current PREVIEW_LABEL, asks for confirmation, flips the boolean, then
runs git add / commit / push so GitHub Pages deploys the change.

If something goes wrong with git, the file edit is still saved on disk
and you can commit + push manually.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path


# ANSI color codes. Modern Windows 10/11 terminals support these once
# we kick the VT escape mode on via `os.system("")`.
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
DIM = "\033[2m"


def enable_ansi_on_windows() -> None:
    if os.name == "nt":
        # Triggers VT100 mode on Windows 10+ cmd.exe; harmless elsewhere.
        os.system("")


WEBSITE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = WEBSITE_DIR / "js" / "preview-config.js"

STATE_RE = re.compile(r"(const\s+PREVIEW_ACTIVE\s*=\s*)(true|false)(\s*;)")
LABEL_RE = re.compile(r'const\s+PREVIEW_LABEL\s*=\s*"([^"]+)"\s*;')


def read_state() -> tuple[bool, str, str]:
    if not CONFIG_FILE.exists():
        print(f"{RED}ERROR: Could not find {CONFIG_FILE}{RESET}")
        print("This script expects to live in <website>/scripts/.")
        sys.exit(1)
    # newline="" preserves CRLF / LF as-is so we don't churn the diff.
    with open(CONFIG_FILE, "r", encoding="utf-8", newline="") as fh:
        text = fh.read()
    state_m = STATE_RE.search(text)
    label_m = LABEL_RE.search(text)
    if not state_m or not label_m:
        print(f"{RED}ERROR: Could not parse {CONFIG_FILE.name}.{RESET}")
        print("Looking for `const PREVIEW_ACTIVE = true|false;` and")
        print("`const PREVIEW_LABEL = \"...\";`.")
        print("Did the file format change? Edit it by hand to fix and re-run.")
        sys.exit(1)
    return state_m.group(2) == "true", label_m.group(1), text


def flip_text(text: str, new_state: bool) -> str:
    new_val = "true" if new_state else "false"
    return STATE_RE.sub(rf"\g<1>{new_val}\g<3>", text, count=1)


def confirm(prompt: str) -> bool:
    try:
        ans = input(prompt).strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    return ans in ("y", "yes")


def run_git(args: list[str]) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=WEBSITE_DIR,
            check=True,
            capture_output=True,
            text=True,
        )
        return True, result.stdout.strip()
    except FileNotFoundError:
        return False, "git is not on PATH"
    except subprocess.CalledProcessError as exc:
        msg = (exc.stderr or exc.stdout or "").strip() or str(exc)
        return False, msg


def main() -> int:
    enable_ansi_on_windows()

    print()
    print(f"{BOLD}{CYAN}===== Mod Preview Flip ====={RESET}")
    print()

    current, label, text = read_state()
    current_word = f"{GREEN}ON{RESET}" if current else f"{RED}OFF{RESET}"
    print(f"  Preview is currently:  {BOLD}{current_word}")
    print(f"  Label:                 {BOLD}{label}{RESET}")
    print()

    new_state = not current
    new_word = "ON" if new_state else "OFF"
    new_color = GREEN if new_state else RED
    verb = "show" if new_state else "hide"

    print(f"  This will flip the preview to {BOLD}{new_color}{new_word}{RESET}, which will:")
    print(f"    - {verb.title()} the preview banner on the home page")
    print(f"    - {verb.title()} the home-page landing card")
    print(f"    - {verb.title()} the nav entry on every page")
    print(f"    - {verb.title()} the link in Toon Forge's nav")
    if not new_state:
        print(f"    - Show the 'archived' notice on preview.html itself")
    print()
    print(f"  Then it will commit the change and push to GitHub.")
    print(f"  {DIM}(GitHub Pages will redeploy in 1-5 minutes.){RESET}")
    print()

    if not confirm(f"{YELLOW}Proceed? (y/n): {RESET}"):
        print()
        print(f"  {DIM}Cancelled. Nothing changed.{RESET}")
        return 0

    # Write the new file content with the same encoding + line endings.
    new_text = flip_text(text, new_state)
    with open(CONFIG_FILE, "w", encoding="utf-8", newline="") as fh:
        fh.write(new_text)
    print()
    print(f"  {GREEN}OK{RESET}  Flipped to {BOLD}{new_color}{new_word}{RESET} in js/preview-config.js")

    # Git workflow.
    print()
    print(f"  {DIM}Staging js/preview-config.js...{RESET}")
    ok, msg = run_git(["add", "js/preview-config.js"])
    if not ok:
        print(f"  {RED}FAIL{RESET}  git add failed: {msg}")
        print(f"  File is saved on disk. Commit + push manually when ready.")
        return 1

    commit_msg = f"preview: flip PREVIEW_ACTIVE to {str(new_state).lower()} ({label})"
    print(f"  {DIM}Committing...{RESET}")
    ok, msg = run_git(["commit", "-m", commit_msg])
    if not ok:
        if "nothing to commit" in msg.lower():
            print(f"  {YELLOW}Nothing to commit{RESET} -- the flag was already that value.")
            return 0
        print(f"  {RED}FAIL{RESET}  git commit failed: {msg}")
        print(f"  File is saved on disk. Commit + push manually when ready.")
        return 1
    print(f"  {GREEN}OK{RESET}  Committed: {DIM}{commit_msg}{RESET}")

    print(f"  {DIM}Pushing to origin/main...{RESET}")
    ok, msg = run_git(["push", "origin", "main"])
    if not ok:
        print(f"  {RED}FAIL{RESET}  git push failed: {msg}")
        print(f"  The commit is in your local repo but not on GitHub yet.")
        print(f"  Run `git push` in the website folder when your connection is back.")
        return 1
    print(f"  {GREEN}OK{RESET}  Pushed.")

    print()
    print(f"  {BOLD}{GREEN}Done.{RESET}  GitHub will deploy in 1-5 minutes.")
    print(f"  {DIM}Hard-refresh (Ctrl+F5) any open browser tab to see the change.{RESET}")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
