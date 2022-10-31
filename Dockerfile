FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
ARG WEBHOOK_URL_ENV=''<your_discord_channel_webhook_URL>'
ENV WEBHOOK_URL=$WEBHOOK_URL_ENV

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python","shopee-scraper.py"]
