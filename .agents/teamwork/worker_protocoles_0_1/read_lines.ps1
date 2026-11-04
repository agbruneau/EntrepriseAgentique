param([int]$start, [int]$end)
$file = 'C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md'
$lines = Get-Content $file
($lines[($start - 1)..($end - 1)]) -join "`n"
