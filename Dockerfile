FROM python:3.8

# Копирование исходного кода приложения в образ
COPY . /app

# Установка зависимостей Python
WORKDIR /app
RUN pip install -r requirements.txt

# Команда, которая будет выполняться при запуске контейнера
CMD ["python", "app.py"]
