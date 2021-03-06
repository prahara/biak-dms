; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Biak Project Document Management Software"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Wahyu Reza Prahara"
#define MyAppURL "http://www.wahyu.org"
#define MyAppExeName "biak.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{5E50BAD8-991C-4D12-A503-5264AA72C17E}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\Biak DMS
DefaultGroupName=Biak Project DMS
OutputBaseFilename=Biak DMS Setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Works\biak-dms\dist\biak.exe"; DestDir: "{app}"; Flags: onlyifdoesntexist confirmoverwrite; Attribs: system
Source: "C:\Works\biak-dms\dist\settings.ini"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Python27\Lib\site-packages\numpy\fft\fftpack_lite.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Python27\Lib\site-packages\numpy\linalg\_umath_linalg.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Program Files (x86)\Intel\OpenCL SDK\2.0\bin\x86\msvcp90.dll"; DestDir: "C:\Program Files (x86)\Intel\OpenCL SDK\2.0\bin\x86\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall
Source: "C:\Windows\System32\oleaut32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\user32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\imm32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\shell32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\ole32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\winmm.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\comdlg32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\advapi32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\advapi32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\crypt32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\msvcrt.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\ws2_32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\winspool.drv"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\gdi32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\kernel32.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
Source: "C:\Windows\System32\ntdll.dll"; DestDir: "C:\Windows\System32\"; Flags: onlyifdoesntexist 32bit sharedfile uninsneveruninstall; Attribs: system
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
