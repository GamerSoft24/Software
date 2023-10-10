Set objVoice = CreateObject("SAPI.SpVoice")
Set objFile = CreateObject("SAPI.SpFileStream.1")

objFile.Open "Windows XP Startup.wav"
objVoice.Speakstream objFile

Set objVoice = CreateObject("SAPI.SpVoice")
Set objFile = CreateObject("SAPI.SpFileStream.1")

objFile.Open "Windows XP Logon Sound.wav"
objVoice.Speakstream objFile

Set objVoice = CreateObject("SAPI.SpVoice")
Set objFile = CreateObject("SAPI.SpFileStream.1")

objFile.Open "Windows XP Logoff Sound.wav"
objVoice.Speakstream objFile

Set objVoice = CreateObject("SAPI.SpVoice")
Set objFile = CreateObject("SAPI.SpFileStream.1")

objFile.Open "Windows XP Shutdown.wav"
objVoice.Speakstream objFile
Wscript.Echo "Did you like the Windows Tunes? Guess what they are!"