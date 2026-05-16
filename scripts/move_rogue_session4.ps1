$source = "C:\Users\N00Bin\OneDrive\Pictures\Screenshots\New folder (2)"
$dest = "G:\ai_projects\nwcb\website\docs\calibration\inbox\rogue-gear-2026-05-15"

New-Item -ItemType Directory -Force -Path $dest | Out-Null

# Session 4 (FINAL): move ALL remaining screenshots — entire Rogue batch complete.
$files = Get-ChildItem -LiteralPath $source -File -Filter '*.png'
$moved = 0
foreach ($file in $files) {
    $newName = $file.Name -replace "Screenshot ", ""
    $dst = Join-Path $dest ("2026-05-15_rogue-gear_" + $newName)
    Move-Item -LiteralPath $file.FullName -Destination $dst -Force
    $moved++
}
Write-Host ("Moved " + $moved + " files to: " + $dest)
$remaining = (Get-ChildItem -LiteralPath $source -File -Filter '*.png' -ErrorAction SilentlyContinue | Measure-Object).Count
Write-Host ("Remaining in source folder: " + $remaining)
