$source = "C:\Users\N00Bin\OneDrive\Pictures\Screenshots\New folder (2)"
$dest = "G:\ai_projects\nwcb\website\docs\calibration\inbox\warlock-gear-mod2-11-2026-05-14"

New-Item -ItemType Directory -Force -Path $dest | Out-Null

# Move every screenshot timestamped through 22:48:44 on 2026-05-14 inclusive —
# that's everything processed in session 1. Files after that timestamp are
# left in the source folder for session 2 to pick up.
$cutoff = "Screenshot 2026-05-14 224844.png"
$files = Get-ChildItem $source -File -Filter "*.png" | Where-Object { $_.Name -le $cutoff }
$moved = 0
foreach ($file in $files) {
    $newName = $file.Name -replace "Screenshot ", ""
    $dst = Join-Path $dest ("2026-05-14_warlock-gear-mod2-11_" + $newName)
    Move-Item -Path $file.FullName -Destination $dst -Force
    $moved++
}
Write-Host ("Moved " + $moved + " files to: " + $dest)
$remaining = (Get-ChildItem $source -File -Filter "*.png" -ErrorAction SilentlyContinue | Measure-Object).Count
Write-Host ("Remaining in source folder for next session: " + $remaining)
