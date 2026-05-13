# Restore images from default Screenshots folder (not "New folder").
# This folder is mixed content (NW + other projects) — restoring all to
# inbox; user can browse and remove non-NW ones.
param(
    [string]$Destination = "G:\ai_projects\nwcb\website\docs\calibration\inbox"
)

$shell = New-Object -ComObject Shell.Application
$recycleBin = $shell.NameSpace(10)
$dest = $shell.NameSpace($Destination)

$items = @($recycleBin.Items())
$filtered = @()
foreach ($it in $items) {
    if ($it.Name -notmatch "\.(png|jpg|jpeg|bmp)$") { continue }
    $orig = $recycleBin.GetDetailsOf($it, 1)
    if ($orig -like "*OneDrive*Pictures*Screenshots" -and $orig -notlike "*New folder*") {
        $filtered += $it
    }
}

Write-Host "Default-folder images to move:" $filtered.Count
Write-Host ""

$count = 0
foreach ($it in $filtered) {
    $count++
    $dest.MoveHere($it, 16)
    if (($count % 25 -eq 0) -or ($count -eq $filtered.Count)) {
        Write-Host ("  [" + $count + "/" + $filtered.Count + "]")
    }
}

Write-Host ""
Write-Host ("Done. Moved " + $count + " files.")
