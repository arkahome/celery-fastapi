# Celery At Work

## Create New Environment

python venv .env 
.\.env\Scripts\activate

## Install Requirements

pip install -r .\requirements.txt

## Redis Server
docker compose up

## Run Celery Worker
celery -A app.celery_worker.celery worker --loglevel=info --pool=gevent

## Flower Dashboard
celery --broker=redis://localhost:6380/0 flower

## Run the FastAPI Application
cd app
uvicorn main:app --reload

## Visit :

http://localhost:8000/docs
