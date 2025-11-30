FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc git && \
    rm -rf /var/lib/apt/lists/*

# Копируем и ставим зависимости + gunicorn
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Копируем весь проект
COPY . .

# Создаём непривилегированного пользователя
RUN adduser --disabled-password --gecos '' django-user

# Создаём нужные папки и даём права уже существующему пользователю
RUN mkdir -p /app/staticfiles /app/media && \
    chown -R django-user:django-user /app /app/staticfiles /app/media

# Переключаемся на пользователя
USER django-user

# Теперь всё работает
RUN python manage.py collectstatic --noinput --clear
RUN python manage.py migrate --noinput

EXPOSE 8000

CMD ["gunicorn", "border_service.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]



# FROM python:3.12-slim

# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1

# # Оставляем WORKDIR в корне контейнера, но копируем всё в /app
# WORKDIR /app

# # Устанавливаем зависимости + git
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     libpq-dev gcc git && \
#     rm -rf /var/lib/apt/lists/*

# # Копируем requirements.txt и устанавливаем зависимости
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Копируем весь проект
# COPY . .

# # ← ВОТ ГЛАВНОЕ ИЗМЕНЕНИЕ:
# # Меняем рабочую директорию туда, где лежит manage.py (то есть корень проекта)
# WORKDIR /app

# # Создаём пользователя
# RUN adduser --disabled-password --gecos '' django-user
# RUN chown -R django-user:django-user /app
# USER django-user

# # collectstatic теперь найдёт manage.py, потому что мы в правильной папке
# RUN python manage.py collectstatic --noinput --clear

# EXPOSE 8000

# CMD ["gunicorn", "border_service.wsgi:application", \
#      "--bind", "0.0.0.0:8000", \
#      "--workers", "4", \
#      "--worker-class", "uvicorn.workers.UvicornWorker"]