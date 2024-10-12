FROM python:3.11 AS base

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "fastapi", "run", "--host", "0.0.0.0", "--port", "8000", "--reload" ]
