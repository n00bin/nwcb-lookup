# List the 122 images from default Screenshots folder (not "New folder").
$shell = New-Object -ComObject Shell.Application
$recycleBin = $shell.NameSpace(10)
$items = @($recycleBin.Items())

$default = @()
foreach ($it in $items) {
    if ($it.Name -notmatch "\.(png|jpg|jpeg|bmp)$") { continue }
    $orig = $recycleBin.GetDetailsOf($it, 1)
    if ($orig -like "*OneDrive*Pictures*Screenshots" -and $orig -notlike "*New folder*") {
        $default += [PSCustomObject]@{
            Name = $it.Name
            Path = $orig
            Deleted = $recycleBin.GetDetailsOf($it, 2)
        }
    }
}

Write-Host "Items in default Screenshots folder:" $default.Count
Write-Host ""

# Show first 30 by filename for spot-check
$default | Sort-Object Name | Select-Object -First 30 | ForEach-Object {
    Write-Host ("  " + $_.Name)
}
Write-Host "..."
$default | Sort-Object Name | Select-Object -Last 5 | ForEach-Object {
    Write-Host ("  " + $_.Name)
}
