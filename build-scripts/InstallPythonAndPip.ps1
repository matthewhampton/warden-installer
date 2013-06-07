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
if (!(Test-Path  ($pythonExe)))
{
    DownloadFile "http://www.python.org/ftp/python/2.7.5/python-2.7.5.msi" "python-2.7.5.msi"
    $exitCode = (Start-Process -FilePath "msiexec.exe" -ArgumentList "/i","python-2.7.5.msi","TARGETDIR=$pwd\Python27","/passive" -Wait -Passthru).ExitCode
    Write-Host "Exit code was: $exitCode"
}

$easyInstallExe = "$pwd\Python27\Scripts\easy_install.exe"
if (!(Test-Path  ($easyInstallExe)))
{
    DownloadFile "http://python-distribute.org/distribute_setup.py" "distribute_setup.py"
    $exitCode = (Start-Process -FilePath $pythonExe -ArgumentList "distribute_setup.py" -Wait -Passthru).ExitCode
    Write-Host "Exit code was: $exitCode"
}

$pipExe = "$pwd\Python27\Scripts\pip.exe"
if (!(Test-Path  ($pipExe)))
{
    $exitCode = (Start-Process -FilePath $easyInstallExe -ArgumentList "pip" -Wait -Passthru).ExitCode
    Write-Host "Exit code was: $exitCode"
}
