$desktop = [Environment]::GetFolderPath("Desktop")
$shortcutPath = Join-Path $desktop "NewXiaoYuan.lnk"

# Remove old shortcut if exists
if (Test-Path $shortcutPath) { Remove-Item $shortcutPath -Force }

$WshShell = New-Object -ComObject WScript.Shell
$lnk = $WshShell.CreateShortcut($shortcutPath)
$lnk.TargetPath = "C:\Users\Administrator\AppData\Local\Programs\Microsoft VS Code\Code.exe"
$lnk.Arguments = "chat --maximize"
$lnk.WorkingDirectory = [Environment]::GetFolderPath("UserProfile")
$lnk.Description = "新建小圆对话"
$lnk.IconLocation = "C:\Users\Administrator\AppData\Local\Programs\Microsoft VS Code\Code.exe,0"
$lnk.Hotkey = "Ctrl+Shift+N"
$lnk.Save()

Write-Host "OK: Shortcut created at $shortcutPath with hotkey Ctrl+Shift+N"
