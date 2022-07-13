@echo off
color 27
title PROGRAM

:start
cls
echo 환영합니다.
pause

:menu
cls
echo 1: 설정
echo 2: 정보
echo 3: 명령어
echo 숫자를 입력하십시오.
set /p input=
if "%input%" == "1" (
	goto option
)else if "%input%" == "2" (
	goto info
)else if "%input%" == "3" (
	goto command
)else (
	cls
	echo 잘못된 입력입니다.
	timeout -t 3
	goto menu
)

:option
cls
echo 1: 프로그램 종료
echo 2: 프로그램 재시작
echo 숫자를 입력하십시오.
set /p input=
if "%input%" == "1" (
	exit
	)
)else if "%input%" == "2" (
	goto start
	)
)else (
	cls
	echo 잘못된 입력입니다.
	timeout -t 3
	goto option
)
pause

:info
cls
echo 개발: PH
echo 프로그램 버전: beta0.3
echo 프로그램 업데이트: https://github.com/anzac9425/Programs
pause
goto menu

:command
cls
echo /help를 입력하여 도움말을 확인하십시오.
echo /exit를 입력하여 메인 메뉴로 이동하십시오.
:command2
set /p input=
if "%input%" == "/help" (
	echo /help를 입력하여 도움말을 확인하십시오.
	echo /exit를 입력하여 메인 메뉴로 이동하십시오.
	echo /shutdown을 입력하여 이 프로그램을 강제로 종료시키십시오.
	goto command2
)else if "%input%" == "/exit" (
	goto menu
)else if "%input%" == "/shutdown" (
	exit
)else (	
	echo 알 수 없는 명령어입니다.
	goto command2
)