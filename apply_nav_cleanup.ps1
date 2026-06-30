$files = Get-ChildItem -Path . -Filter *.html
foreach ($f in $files) {
    $text = Get-Content -Raw $f.FullName
    $new = $text
    $new = $new -replace [regex]::Escape('<li><a href="venue.html">Lokasi</a></li>'), '<li><a href="blog.html">Blog</a></li>'
    $new = $new -replace [regex]::Escape('<li><a href="venue.html" class="active">Lokasi</a></li>'), '<li><a href="blog.html" class="active">Blog</a></li>'
    $new = $new -replace [regex]::Escape('<li><a href="speaker-details.html" class="active">Detail Pembicara</a></li>'), ''
    $new = $new -replace [regex]::Escape('<li><a href="speaker-details.html">Detail Pembicara</a></li>'), ''
    $new = [System.Text.RegularExpressions.Regex]::Replace($new, '<a href="#" class="btn-outline">.*?<i class="bi bi-share"></i>.*?Share Profile.*?</a>\s*', '', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    if ($new -ne $text) {
        Set-Content -Path $f.FullName -Value $new -Encoding utf8
        Write-Output "Updated $($f.Name)"
    }
}
