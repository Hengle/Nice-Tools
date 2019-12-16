@echo off

cd pb_proto
REM 生成二进制文件pb(首先删除在重新生成)
rd /s /q ..\pb_lua\pb
md ..\pb_lua\pb
set pbPath=..\pb_lua\pb
set pb=.pb
for %%i in (*.*) do (
    echo %%i
    ..\protoc -o %pbPath%\%%i%pb% %%i
)
echo pb create success


cd ..\pb_lua\pb
SetLocal EnableDelayedExpansion
REM 要查找的文件类型
set ext=*.pb%
REM 重新命名文件
for /r %%a in (!ext!) do (
    REM 文件名
    set fn=%%~na
    REM 后缀
    set en=%%~xa
    REM 把字符串的最后4个字符赋值给变量hou
    set hou=!fn:~0,-6!
    echo !hou!!en!
    rename "%%a" "!hou!!en!"
)
echo pb rename success
echo.

REM 项目中pb文件存放目录
set destPath=E:\source\client\xxx\Assets\StreamingAssets\lua\pb

rd /s /q %destPath%
md %destPath%

echo copy to %destPath%
::xcopy ..\pb %destPath% /s /e


cd ..\..\ProtoToLua
echo .
@python msgid-gen-lua.py


pause