
# project setup

docker-compython3 -m venv venv_taskmanager

source venv_taskmanager/bin/activate

Python3 -m pip install -r requirements.txt

docker-compose up -d

python3 manage.py runserver
