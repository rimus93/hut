TITLE "Backup Progress DB + Archieve"

@ECHO off
REM "Cvetnoi fon"
COLOR 3f
REM "Papka Progress"
SET dlcbin=C:\Progress10B\bin
REM "Papka DB"
SET db=D:\DB\ub
REM "Tekushaya data"
SET day=%date:~0,2%
REM "Skolko dnei hranit backup + ukazanie proshloi dati backupa"
IF %day% LEQ 14 (
SET /A pastday=%day%+17
) ELSE (
SET /A pastday=%day%-14
)
REM "Proverka dati na razryadnost"
IF %day% LSS 10 (
SET bkpfile=ub.bkp_%date:~1,1%
) ELSE (
SET bkpfile=ub.bkp_%day%
)
REM "Stariy zaarhivirovanniy backup"
SET bkpfileold=ub.bkp_%pastday%.7z
REM "Papka novogo backupa"
SET newbkp=D:\backup_BD
REM "Papka starogo backupa"
SET oldbkp=D:\backup_BD\OLD_BKP
REM "Papka backupa na vneshnem diske"
SET extbkp=X:\Murmansk_DB_Backup
REM "Papka logov"
SET logdir=D:\backup_BD
REM "Papka arhivatora"
SET archdir=D:\backup_BD\7-Zip

REM "Nachalo loga"
ECHO ----------------------------------------------------------->>%logdir%\bkplog.txt

SETlocal EnableDelayedExpansion

REM "Proverka nalichiya papok"
IF NOT EXIST %newbkp% md %newbkp%
IF NOT EXIST %oldbkp% md %oldbkp%
IF NOT EXIST %extbkp% md %extbkp%

ECHO %DATE% %TIME:~0,8% Kopirovanie starogo faila structury BD "ub.st">>%logdir%\bkplog.txt
IF EXIST %newbkp%\ub.st (
COPY /y /z %newbkp%\ub.st %oldbkp%\
) ELSE (
ECHO %DATE% %TIME:~0,8% Ne naiden stariy fail structury BD "ub.st" v kataloge "%newbkp%">>%logdir%\bkplog.txt 
)

ECHO %DATE% %TIME:~0,8% Udalenie predidushih localnih backupov BD v kataloge "%oldbkp%">>%logdir%\bkplog.txt
DEL /Q %oldbkp%\ub.bkp*

ECHO %DATE% %TIME:~0,8% Kopirovanie predidushih localnih backupov BD v katalog "%oldbkp%">>%logdir%\bkplog.txt
COPY /y /z %newbkp%\ub.bkp* %oldbkp%\

ECHO %DATE% %TIME:~0,8% Udalenie predidushih localnih backupov BD v kataloge "%newbkp%">>%logdir%\bkplog.txt
DEL  /Q %newbkp%\ub.bkp*

ECHO %DATE% %TIME:~0,8% Sozdanie backupa BD "%bkpfile%">>%logdir%\bkplog.txt 
call %dlcbin%\probkup online %db% %newbkp%\%bkpfile%

ECHO %DATE% %TIME:~0,8% Arhivirovanie backupa BD "%bkpfile%" v "%bkpfile%.7z">>%logdir%\bkplog.txt
%archdir%\7z.exe a %newbkp%\%bkpfile%.7z %newbkp%\%bkpfile% -y -sdel

ECHO %DATE% %TIME:~0,8% Kopirovanie novogo faila structury BD "ub.st" v "%newbkp%">>%logdir%\bkplog.txt  
IF EXIST %db%.st (
COPY /y /z %db%.st %newbkp%\
) ELSE (
ECHO %DATE% %TIME:~0,8% Ne naiden fail struktury BD "ub.st" v kataloge "%db%">>%logdir%\bkplog.txt
)

ECHO %DATE% %TIME:~0,8% Podkluchaem setevoi disk X:>>%logdir%\bkplog.txt
REM NET USE X: /delete /y
NET USE X: \\172.168.0.1\backup /u:172.168.0.1\userlogin userpassword>>%logdir%\bkplog.txt

ECHO %DATE% %TIME:~0,8% Kopirovanie novogo faila struktury BD "ub.st" na vneshniy disk>>%logdir%\bkplog.txt
IF EXIST %newbkp%\ub.st (
COPY /y /z %newbkp%\ub.st %extbkp%\
) ELSE (
ECHO %DATE% %TIME:~0,8% Ne naiden staryi fail struktury BD "ub.st" v kataloge "%newbkp%">>%logdir%\bkplog.txt
)

ECHO %DATE% %TIME:~0,8% Udalenie starogo vneshnego backupa BD "%bkpfileold%" v kataloge "%extbkp%">>%logdir%\bkplog.txt 
IF EXIST %extbkp%\%bkpfileold% (
DEL /Q %extbkp%\%bkpfileold%
) ELSE (
ECHO %DATE% %TIME:~0,8% V kataloge "%extbkp%" ne naiden strariy udalenniy backup "%bkpfileold%">>%logdir%\bkplog.txt 
)

ECHO %DATE% %TIME:~0,8% Kopirovanie novogo backupa BD "%bkpfile%.7z" na vneshniy disk>>%logdir%\bkplog.txt
IF EXIST %newbkp%\%bkpfile%.7z (
COPY /y /z %newbkp%\%bkpfile%.7z %extbkp%\
) ELSE (
ECHO %DATE% %TIME:~0,8% Ne naiden backup BD "%bkpfile%.7z" v kataloge "%newbkp%">>%logdir%\bkplog.txt
)

REM ECHO %DATE% %TIME:~0,8% Otkluchaem setevoi disk X:>>%logdir%\bkplog.txt
REM NET USE X: /d>>%logdir%\bkplog.txt
ECHO %DATE% %TIME:~0,8% Rezervnoe kopirovanie zaversheno>>%logdir%\bkplog.txt
REM PAUSE
EXIT