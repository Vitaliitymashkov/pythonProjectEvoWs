FROM python:3.6-stretch
MAINTAINER vitalii.tymashkov@gmail.com

# устанавливаем параметры сборки
RUN apt-get update && \
 apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# проверяем окружение python
RUN python3 --version
RUN pip3 --version

# задаем рабочую директорию для контейнера
RUN mkdir /app
WORKDIR /app

# копируем все файлы из корня проекта в рабочую директорию
ADD . /app/
# устанавливаем зависимости python
RUN pip install -r requirements.txt

RUN python3 /app/init_db.py

EXPOSE 8080

# запускаем приложение Python
CMD ["python3", "main.py"]
