$file = 'C:\Github\EntrepriseAgentique\documents\DOCUMENT_TEXT_MAP.md'
$lines = Get-Content $file
$pages = [System.Collections.Generic.Dictionary[int, int]]::new()
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '^## \[Page (\d+)\]') {
        $p = [int]$matches[1]
        if ($p -ge 78 -and $p -le 146) {
            $pages[$p] = $i + 1
        }
    }
}
foreach ($k in ($pages.Keys | Sort-Object)) {
    Write-Output ("Page {0} -> Line {1}" -f $k, $pages[$k])
}
