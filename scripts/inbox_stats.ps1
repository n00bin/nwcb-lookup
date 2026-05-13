$files = Get-ChildItem "G:\ai_projects\nwcb\website\docs\calibration\inbox" -File -Filter "*.png"
$totalSize = ($files | Measure-Object Length -Sum).Sum
Write-Host ("Total PNG files: " + $files.Count)
Write-Host ("Total size: " + [math]::Round($totalSize / 1GB, 2) + " GB")
