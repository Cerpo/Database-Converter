IF NOT EXIST venv\ (python -m venv venv)
cd ./venv/Scripts
call activate.bat
cd ../../
pip install -r requirements.txt
python -m src.main
pause