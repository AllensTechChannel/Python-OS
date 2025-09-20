powershell -Command ^
  "$filePath = 'ownercompany.txt';" ^
  "$company = Read-Host 'Enter your company';" ^
  "if ([string]::IsNullOrWhiteSpace($company)) { $company = 'org name' };" ^
  
  "Set-Content -Path $filePath -Value $company;" ^
  
 
  "Write-Host \"Company set as $company!\";"^
  "Start-Sleep -Seconds 2"
