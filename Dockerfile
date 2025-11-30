# app/Dockerfile  ← положи прямо рядом с manage.py

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Системные зависимости (только для psycopg2 и gunicorn)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Не-root пользователь
RUN adduser --disabled-password --gecos '' django-user
RUN chown -R django-user:django-user /app
USER django-user

# collectstatic при сборке (можно вынести в entrypoint, но для начала так проще)
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "project.wsgi:application", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "4", \
     "--worker-class", "uvicorn.workers.UvicornWorker"]