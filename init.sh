python -m venv dev_api 
source ./dev_api/scripts/activate
pip install Flask
echo ".read create.sql" | sqlite3 devs.db
./main.py