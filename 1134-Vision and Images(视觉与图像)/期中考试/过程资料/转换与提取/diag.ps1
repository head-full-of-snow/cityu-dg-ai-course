$ErrorActionPreference = 'SilentlyContinue'
$clsid = (Get-ItemProperty 'Registry::HKEY_CLASSES_ROOT\PowerPoint.Application\CLSID').'(default)'
Write-Output ("PowerPoint.Application CLSID: " + $clsid)
$ls32 = (Get-ItemProperty ("Registry::HKEY_CLASSES_ROOT\CLSID\" + $clsid + "\LocalServer32")).'(default)'
Write-Output ("LocalServer32: " + $ls32)

foreach ($p in @('KWPP.Application','ET.Application','WPS.Application','Word.Application','Kwps.Application')) {
    $c = (Get-ItemProperty ("Registry::HKEY_CLASSES_ROOT\" + $p + "\CLSID")).'(default)'
    if ($c) {
        $srv = (Get-ItemProperty ("Registry::HKEY_CLASSES_ROOT\CLSID\" + $c + "\LocalServer32")).'(default)'
        Write-Output ($p + " -> " + $c + " server: " + $srv)
    } else {
        Write-Output ($p + " -> NOT REGISTERED")
    }
}
