Get-ChildItem -LiteralPath 'G:\ai_projects\nwcb\website\docs\calibration\inbox' -Directory | ForEach-Object {
    $count = (Get-ChildItem -LiteralPath $_.FullName -File -Filter '*.png' -Recurse | Measure-Object).Count
    Write-Host ($_.Name + ': ' + $count + ' images')
}
