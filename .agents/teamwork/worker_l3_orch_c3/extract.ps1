$allLines = Get-Content -Path 'C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md'
$allLines[22343..23577] | Set-Content -Path 'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_l3_orch_c3\ch22_raw.txt'
$allLines[23578..24347] | Set-Content -Path 'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_l3_orch_c3\ch23_raw.txt'
$allLines[24348..26335] | Set-Content -Path 'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_l3_orch_c3\ch24_raw.txt'
$allLines[26336..27187] | Set-Content -Path 'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_l3_orch_c3\ch25_raw.txt'
$allLines[27188..27584] | Set-Content -Path 'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_l3_orch_c3\ch26_raw.txt'
Write-Host "Extractions successfully written."
