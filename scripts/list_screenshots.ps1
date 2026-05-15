$folder = 'C:\Users\N00Bin\OneDrive\Pictures\Screenshots\New folder (2)'
Get-ChildItem -LiteralPath $folder -File -Filter '*.png' | Sort-Object Name | Select-Object -Skip 27 -First 50 | Select-Object -ExpandProperty Name
