# Move 3 sample images from default Screenshots folder out of recycle bin
# to a temp inspection folder. Picks one early, one mid, one recent.
param(
    [string]$Destination = "G:\ai_projects\nwcb\website\docs\calibration\sample_inspect"
)

New-Item -ItemType Directory -Force -Path $Destination | Out-Null

$shell = New-Object -ComObject Shell.Application
$recycleBin = $shell.NameSpace(10)
$dest = $shell.NameSpace($Destination)
$items = @($recycleBin.Items())

$default = @()
foreach ($it in $items) {
    if ($it.Name -notmatch "\.(png|jpg|jpeg|bmp)$") { continue }
    $orig = $recycleBin.GetDetailsOf($it, 1)
    if ($orig -like "*OneDrive*Pictures*Screenshots" -and $orig -notlike "*New folder*") {
        $default += $it
    }
}

Write-Host "Total default-folder items:" $default.Count

# Pick first, middle, last by name
$sorted = $default | Sort-Object Name
$samples = @($sorted[0], $sorted[[int]($sorted.Count / 2)], $sorted[$sorted.Count - 1])

foreach ($s in $samples) {
    $orig = $recycleBin.GetDetailsOf($s, 1)
    Write-Host ("Moving sample: " + $s.Name + " (from " + $orig + ")")
    $dest.MoveHere($s, 16)
}

Write-Host "Done. 3 samples in" $Destination
