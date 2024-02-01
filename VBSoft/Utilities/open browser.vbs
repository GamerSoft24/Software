MsgBox "Hello! We will be opening Google Chrome for you. If it is not installed, Microsoft Edge will be opened. Please wait...", vbInformation, "Open Browser"

Dim chrome
chrome = "C:\Progra~2\Google\Chrome\Application\chrome.exe"
Dim edge
edge = "C:\Progra~2\Microsoft\Edge\Application\msedge.exe"

Set objFSO = CreateObject("Scripting.FileSystemObject")
If objFSO.FileExists(chrome) Then
    Set objShell = CreateObject("WScript.Shell")
    objShell.Run chrome, 1, True
    Set objShell = Nothing
Else
    Set objShell = CreateObject("WScript.Shell")
    objShell.Run edge, 1, True
    Set objShell = Nothing
End If

Set objFSO = Nothing
