# Pick evenly-spaced inbox files for sampling.
# Returns ~30 filenames: 15 from May 10, 10 from May 11, 5 from earlier.
param(
    [int]$May10Count = 15,
    [int]$May11Count = 10,
    [int]$EarlierCount = 5
)

$inbox = "G:\ai_projects\nwcb\website\docs\calibration\inbox"
$all = Get-ChildItem $inbox -File -Filter "Screenshot*.png" | Sort-Object Name

$may10 = $all | Where-Object { $_.Name -like "*2026-05-10*" }
$may11 = $all | Where-Object { $_.Name -like "*2026-05-11*" }
$earlier = $all | Where-Object { $_.Name -like "*2026-05-0*" -and $_.Name -notlike "*2026-05-10*" -and $_.Name -notlike "*2026-05-11*" }

function PickEven($list, $n) {
    if ($list.Count -le $n) { return $list }
    $step = [math]::Floor($list.Count / $n)
    $result = @()
    for ($i = 0; $i -lt $n; $i++) {
        $idx = [math]::Min($i * $step, $list.Count - 1)
        $result += $list[$idx]
    }
    return $result
}

$picks10 = PickEven $may10 $May10Count
$picks11 = PickEven $may11 $May11Count
$picksEarlier = PickEven $earlier $EarlierCount

Write-Host "May 10 picks ($($picks10.Count)):"
$picks10 | ForEach-Object { Write-Host ("  " + $_.Name) }
Write-Host ""
Write-Host "May 11 picks ($($picks11.Count)):"
$picks11 | ForEach-Object { Write-Host ("  " + $_.Name) }
Write-Host ""
Write-Host "Earlier picks ($($picksEarlier.Count)):"
$picksEarlier | ForEach-Object { Write-Host ("  " + $_.Name) }
