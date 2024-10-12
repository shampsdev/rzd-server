FROM python:3.10.12 AS base

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y libsndfile1

COPY . .

CMD [ "fastapi", "run", "--host", "0.0.0.0", "--port", "8000", "--reload" ]
