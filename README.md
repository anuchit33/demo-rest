#Install Project
virtualenv -p python3 env
source env/bin/activate

pip install -r requirements.txt 
python manage.py makemigrations customer