# Sort inbox by filename (timestamps embedded), show most recent
$files = Get-ChildItem "G:\ai_projects\nwcb\website\docs\calibration\inbox" -File -Filter "*.png" | Sort-Object Name -Descending
Write-Host ("Total files: " + $files.Count)
Write-Host ""
Write-Host "Most recent 40 (by filename timestamp):"
$files | Select-Object -First 40 | ForEach-Object { Write-Host ("  " + $_.Name) }
