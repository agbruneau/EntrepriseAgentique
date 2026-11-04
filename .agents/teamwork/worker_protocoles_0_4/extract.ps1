$lines = Get-Content -Path 'C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md'
$p78 = 0; $p115 = 0; $p128 = 0; $p140 = 0; $p146 = 0

for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^## \[Page 78\]') { $p78 = $i }
    if ($lines[$i] -match '^## \[Page 115\]') { $p115 = $i }
    if ($lines[$i] -match '^## \[Page 128\]') { $p128 = $i }
    if ($lines[$i] -match '^## \[Page 140\]') { $p140 = $i }
    if ($lines[$i] -match '^## \[Page 146\]') { $p146 = $i; break }
}

Write-Host "Indices: p78=$p78, p115=$p115, p128=$p128, p140=$p140, p146=$p146"
$lines[$p78..($p115-1)] | Set-Content -Path 'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_protocoles_0_4\ch7_8_9_text.txt'
$lines[$p115..($p128-1)] | Set-Content -Path 'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_protocoles_0_4\ch10_text.txt'
$lines[$p128..($p140-1)] | Set-Content -Path 'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_protocoles_0_4\ch11_text.txt'
$lines[$p140..($p146-1)] | Set-Content -Path 'c:\Github\EntrepriseAgentique\.agents\teamwork\worker_protocoles_0_4\ch12_text.txt'
