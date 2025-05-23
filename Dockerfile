FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Chrome and Chromedriver
RUN apt-get update && apt-get install -y \
    wget gnupg unzip curl \
    chromium chromium-driver

# Environment variables
ENV PATH="/usr/lib/chromium/:${PATH}"
ENV CHROME_BIN="/usr/bin/chromium"


WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ./app

# CMD ["gunicorn", "techNews.wsgi:application", "--bind", "0.0.0.0:8000"] --- for production
