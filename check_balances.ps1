$path='c:\Users\Sanju\OneDrive - CromptonConcepts\Sharepoint - Documents\Clients\Application development\Apps\TIA+QUEUE\Crompton_TIA_QUEUE\Crompton_TIA_Queue.html'
$content=Get-Content -Raw -Path $path
$script=[regex]::Match($content,'<script>([\s\S]*?)</script>').Groups[1].Value
$lines=$script -split '\r?\n'
$braces=0; $parens=0; $brackets=0
for($i=0;$i -lt $lines.Length;$i++){
    $line=$lines[$i]
    foreach($ch in $line.ToCharArray()){
        switch($ch){
            '{'{$braces++}
            '}'{$braces--}
            '('{$parens++}
            ')'{ $parens--}
            '['{$brackets++}
            ']'{$brackets--}
        }
    }
    if($braces -gt 0){ Write-Output "line $($i+1) braces now $braces" }
    if($braces -lt 0 -or $parens -lt 0 -or $brackets -lt 0){
        Write-Output "imbalance negative at line $($i+1): braces=$braces parens=$parens brackets=$brackets"
        break
    }
}
Write-Output "final counts braces=$braces parens=$parens brackets=$brackets"
