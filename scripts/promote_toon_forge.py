"""Move Toon Forge from /prototypes/ to website root, fixing relative paths."""
from pathlib import Path

src = Path("G:/ai_projects/nwcb/website/prototypes/toon-forge.html")
dst = Path("G:/ai_projects/nwcb/website/toon-forge.html")

content = src.read_text(encoding="utf-8")

# Fix relative paths: ../X → X (since we're going up one directory level)
# script src="../data/X.js" → script src="data/X.js"
content = content.replace('script src="../data/', 'script src="data/')
content = content.replace('script src="../js/',   'script src="js/')

# href="../mekaniks.html..." → href="mekaniks.html..."
content = content.replace('href="../mekaniks.html', 'href="mekaniks.html')

# Update <title>
content = content.replace(
    "<title>Toon Forge (Prototype) — NWCB</title>",
    "<title>Toon Forge — NWCB</title>"
)

# Replace badge: "Prototype" → "Experimental" with explanatory tooltip
content = content.replace(
    '<span class="badge">Prototype</span>',
    '<span class="badge" title="Work-in-progress. Numbers may not be 100% accurate yet — help us improve by using the ✎ pencil to fix anything wrong.">Experimental</span>'
)

dst.write_text(content, encoding="utf-8")
remaining = content.count("../")
print(f"Wrote {dst}")
print(f"Remaining '../' references: {remaining}")
if remaining:
    # Show the lines so we can spot anything we missed
    for i, line in enumerate(content.split("\n"), 1):
        if "../" in line:
            print(f"  line {i}: {line.strip()[:120]}")
