$source = "C:\Users\N00Bin\OneDrive\Pictures\Screenshots\New folder (2)"
$destRogue  = "G:\ai_projects\nwcb\website\docs\calibration\inbox\rogue-powers-2026-05-15"
$destWizard = "G:\ai_projects\nwcb\website\docs\calibration\inbox\wizard-powers-2026-05-16"

New-Item -ItemType Directory -Force -Path $destRogue  | Out-Null
New-Item -ItemType Directory -Force -Path $destWizard | Out-Null

$files = Get-ChildItem -LiteralPath $source -File -Filter '*.png'
$movedR = 0; $movedW = 0
foreach ($file in $files) {
    if ($file.Name -like "Screenshot 2026-05-15 *.png") {
        $newName = $file.Name -replace "Screenshot ", ""
        $dst = Join-Path $destRogue ("2026-05-15_rogue-powers_" + $newName)
        Move-Item -LiteralPath $file.FullName -Destination $dst -Force
        $movedR++
    } elseif ($file.Name -like "Screenshot 2026-05-16 *.png") {
        $newName = $file.Name -replace "Screenshot ", ""
        $dst = Join-Path $destWizard ("2026-05-16_wizard-powers_" + $newName)
        Move-Item -LiteralPath $file.FullName -Destination $dst -Force
        $movedW++
    }
}
Write-Host ("Moved " + $movedR + " Rogue power screenshots to: " + $destRogue)
Write-Host ("Moved " + $movedW + " Wizard power screenshots to: " + $destWizard)
$remaining = (Get-ChildItem -LiteralPath $source -File -Filter '*.png' -ErrorAction SilentlyContinue | Measure-Object).Count
Write-Host ("Remaining in source folder: " + $remaining)
