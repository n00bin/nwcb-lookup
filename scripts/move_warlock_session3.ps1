$source = "C:\Users\N00Bin\OneDrive\Pictures\Screenshots\New folder (2)"
$dest = "G:\ai_projects\nwcb\website\docs\calibration\inbox\warlock-gear-mod2-13-2026-05-15"

New-Item -ItemType Directory -Force -Path $dest | Out-Null

# Move all remaining screenshots — session 3 finished the legacy gear batch.
$files = Get-ChildItem $source -File -Filter "*.png"
$moved = 0
foreach ($file in $files) {
    $newName = $file.Name -replace "Screenshot ", ""
    $dst = Join-Path $dest ("2026-05-15_warlock-gear_" + $newName)
    Move-Item -Path $file.FullName -Destination $dst -Force
    $moved++
}
Write-Host ("Moved " + $moved + " files to: " + $dest)
$remaining = (Get-ChildItem $source -File -Filter "*.png" -ErrorAction SilentlyContinue | Measure-Object).Count
Write-Host ("Remaining in source folder: " + $remaining)
