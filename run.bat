@echo off

if not exist "venv\Scripts\activate.bat" (
    py -m venv venv >nul 2>&1 || (
        python -m venv venv >nul 2>&1 || (
            python3 -m venv venv >nul 2>&1 || (
                echo ОШИБКА: Не удалось создать виртуальное окружение
                pause
                exit
            )
        )
    )
)

call venv\Scripts\activate.bat >nul
pip install requests --disable-pip-version-check >nul 2>&1

:: Запускаем основной скрипт
python run.py