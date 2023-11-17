cd ./venv/Scripts
call activate.bat
pip freeze
cd ../../
python -m src.main
pause