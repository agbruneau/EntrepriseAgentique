param([string]$file, [string]$pattern)
$lines = Get-Content $file
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match $pattern) {
        Write-Host "=== Line $i ==="
        $start = [Math]::Max(0, $i - 5)
        $end = [Math]::Min($lines.Count - 1, $i + 5)
        $lines[$start..$end] | ForEach-Object { Write-Host $_ }
    }
}
