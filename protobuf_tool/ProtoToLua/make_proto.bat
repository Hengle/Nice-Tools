@::make_proto.bat
@echo off

set UnityProtolDir=..\pb_lua\pb
set LuaProtoSrcDir=..\pb_proto
set LuaPluginDir=.\plugin

if exist "%UnityProtolDir%" rd /s /q "%UnityProtolDir%"
md "%UnityProtolDir%"


cd %LuaProtoSrcDir%
setlocal enabledelayedexpansion
for /f %%i in ('dir /b proto "*.proto"') do (
	echo..\protoc.exe -o %UnityProtolDir%\%%~ni.pb %%i 
	..\protoc.exe -o %UnityProtolDir%\%%~ni.pb %%i 
)
	
cd ..
cd ProtoToLua
cd "%LuaPluginDir%"
@python msgid-gen-lua.py

echo DONE

pause
exit

:StringLenth 
	set theString=%~1
	if not defined theString goto :eof 
	set Return=0 
:StringLenth_continue 
	set /a Return+=1
	set theString=%theString:~,-1%
	if defined theString goto StringLenth_continue 
	if not "%2"=="" set %2=%Return%
goto :eof