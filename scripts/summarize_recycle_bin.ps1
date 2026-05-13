# Group recycle bin images by source folder and deletion date
$shell = New-Object -ComObject Shell.Application
$recycleBin = $shell.NameSpace(10)
$items = @($recycleBin.Items())

$images = $items | Where-Object { $_.Name -match '\.(png|jpg|jpeg|bmp)$' }

$rows = foreach ($img in $images) {
    [PSCustomObject]@{
        Name = $img.Name
        OrigPath = $recycleBin.GetDetailsOf($img, 1)
        Deleted = $recycleBin.GetDetailsOf($img, 2)
        Size = $recycleBin.GetDetailsOf($img, 3)
    }
}

Write-Host "=== By Source Folder ==="
$rows | Group-Object OrigPath | Sort-Object Count -Descending | ForEach-Object {
    Write-Host ("{0,5}  {1}" -f $_.Count, $_.Name)
}

Write-Host ""
Write-Host "=== By Deletion Date (date only, ignoring time) ==="
$rows | ForEach-Object {
    $dateOnly = ($_.Deleted -replace '\?', '') -replace ' .*', ''
    [PSCustomObject]@{ DateOnly = $dateOnly; Row = $_ }
} | Group-Object DateOnly | Sort-Object Name | ForEach-Object {
    Write-Host ("{0,5}  deleted on {1}" -f $_.Count, $_.Name)
}
