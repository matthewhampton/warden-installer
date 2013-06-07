$storageDir = $pwd
$webclient = New-Object System.Net.WebClient

Function DownloadFile($url, $filename)
{
    $file = "$storageDir\$filename"

    if (!(Test-Path  ($file)))
    {
        $webclient.DownloadFile($url,$file)
    }
}

$pythonExe = "$pwd\Python27\python.exe"
if (Test-Path  ($pythonExe))
{
    DownloadFile "http://www.python.org/ftp/python/2.7.5/python-2.7.5.msi" "python-2.7.5.msi"
    $exitCode = (Start-Process -FilePath "msiexec.exe" -ArgumentList "/x","python-2.7.5.msi","TARGETDIR=$pwd\Python27","/passive" -Wait -Passthru).ExitCode
    Write-Host "Exit code was: $exitCode"
}

$pythonDir = "$pwd\Python27"
if (Test-Path  ($pythonDir))
{
    Remove-Item -Recurse -Force $pythonDir
}