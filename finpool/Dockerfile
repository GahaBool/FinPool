#Базовый образ Ubuntu
FROM ubuntu:20.04

#Обновляем пакеты и устанавливаем зависимости 
RUN apt-get update && apt-get install -y python3-pip python3-dev libpq-dev

#Устанавливаем рабочию DIR
WORKDIR /finpool/

#Копируем зависимости проекта
COPY requirements.txt /finpool/

#Устанавливаем зависимости 
RUN pip3 install -r requirements.txt

#Копируем код проекта
COPY . /finpool/

#Запускаем сервер Django
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
