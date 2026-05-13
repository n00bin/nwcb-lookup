param(
    [string]$Destination = "G:\ai_projects\nwcb\website\docs\calibration\inbox",
    [string]$SourceFilter = "Screenshots\New folder",
    [switch]$DryRun = $false
)

$shell = New-Object -ComObject Shell.Application
$recycleBin = $shell.NameSpace(10)
$dest = $shell.NameSpace($Destination)

if ($null -eq $dest) {
    Write-Error "Destination not found"
    exit 1
}

$items = @($recycleBin.Items())
$filtered = @()
foreach ($it in $items) {
    if ($it.Name -notmatch "\.(png|jpg|jpeg|bmp)$") { continue }
    $orig = $recycleBin.GetDetailsOf($it, 1)
    if ($orig -like "*$SourceFilter*") {
        $filtered += $it
    }
}

Write-Host "Recycle bin total:" $items.Count
Write-Host "Matching images:" $filtered.Count
Write-Host "Destination:" $Destination
Write-Host "Dry run:" $DryRun
Write-Host ""

if ($DryRun) {
    Write-Host "DRY RUN. First 5 matches:"
    foreach ($it in ($filtered | Select-Object -First 5)) {
        $orig = $recycleBin.GetDetailsOf($it, 1)
        Write-Host ("  " + $it.Name + " from " + $orig)
    }
    exit 0
}

$count = 0
$total = $filtered.Count
$startTime = Get-Date

foreach ($item in $filtered) {
    $count++
    $dest.MoveHere($item, 16)
    if (($count % 100 -eq 0) -or ($count -eq $total)) {
        $elapsed = (Get-Date) - $startTime
        Write-Host ("  [" + $count + "/" + $total + "]  elapsed " + [int]$elapsed.TotalSeconds + "s")
    }
}

Write-Host ""
Write-Host ("Done. Moved " + $count + " files.")
