FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
ARG WEBHOOK_URL_ENV='https://discord.com/api/webhooks/1036137783166763050/ZNT6vAhyyZcjbY0y57MkISW7uc-l6QdGYMT3ZxKD6GYFpQt0JJPnfPDL0RJ0ocgcMn7D'
ENV WEBHOOK_URL=$WEBHOOK_URL_ENV

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python","shopee-scraper.py"]