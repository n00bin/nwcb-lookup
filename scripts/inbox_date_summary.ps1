# Group inbox files by date (extracted from filename timestamp)
$files = Get-ChildItem "G:\ai_projects\nwcb\website\docs\calibration\inbox" -File -Filter "*.png"
$buckets = @{}
foreach ($f in $files) {
    if ($f.Name -match "Screenshot (\d{4}-\d{2}-\d{2})") {
        $date = $matches[1]
        if (-not $buckets.ContainsKey($date)) { $buckets[$date] = 0 }
        $buckets[$date]++
    }
}
Write-Host "By date (extracted from filename):"
$buckets.GetEnumerator() | Sort-Object Name | ForEach-Object {
    Write-Host ("  " + $_.Name + "  " + $_.Value)
}
