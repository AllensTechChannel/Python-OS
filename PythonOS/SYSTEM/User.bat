powershell -Command ^
  "$filePath = 'owner.txt';" ^
  "$name = Read-Host 'Enter your Username';" ^
  "if ([string]::IsNullOrWhiteSpace($name)) { $name = 'user name' };" ^
  "Set-Content -Path $filePath -Value $name;" ^
  "Write-Host \"Username set as $name!\";"^
  "Start-Sleep -Seconds 2"
