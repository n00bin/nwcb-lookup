$folder = 'C:\Users\N00Bin\OneDrive\Pictures\Screenshots\New folder (2)'
$skip = [int]$args[0]
$take = if ($args[1]) { [int]$args[1] } else { 50 }
Get-ChildItem -LiteralPath $folder -File -Filter '*.png' | Sort-Object Name | Select-Object -Skip $skip -First $take | Select-Object -ExpandProperty Name
