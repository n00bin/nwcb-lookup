# List image files in Windows Recycle Bin
$shell = New-Object -ComObject Shell.Application
$recycleBin = $shell.NameSpace(10)
$items = @($recycleBin.Items())

Write-Host "Total items in recycle bin: $($items.Count)"

$images = $items | Where-Object { $_.Name -match '\.(png|jpg|jpeg|bmp)$' }
Write-Host "Image files: $($images.Count)"
Write-Host ""

$idx = 0
foreach ($img in $images) {
    $idx++
    $deleted = $recycleBin.GetDetailsOf($img, 2)
    $origPath = $recycleBin.GetDetailsOf($img, 1)
    $size = $recycleBin.GetDetailsOf($img, 3)
    Write-Host ("[{0}] {1}  ({2})  deleted: {3}  from: {4}" -f $idx, $img.Name, $size, $deleted, $origPath)
}
