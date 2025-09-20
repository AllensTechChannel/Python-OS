powershell -Command ^
  "$filePath = 'pwd.txt';" ^
  "$name = Read-Host 'Enter your Password';" ^
  "if ([string]::IsNullOrWhiteSpace($name)) { $name = 'user name' };" ^
  "Set-Content -Path $filePath -Value $name;" ^
  "Write-Host \"Password set as $name!\";" ^
  "Start-Sleep -Seconds 2"
