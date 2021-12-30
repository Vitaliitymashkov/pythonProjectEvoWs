# Завдання №2

## Потрібно написати веб-сервіс. 
На головній сторінці форма з полем введення імені та кнопкою "Привітатись". При натисканні на кнопку, якщо ім'я зустрілося вперше, виведи "Привіт, <Ім'я>". Якщо таке ім'я вже зустрічалося, виведи "Вже бачилися, ім'я".

## Також 
на головній має бути посилання, при натисканні на яке потрібно показати список усіх, з ким уже привіталися.

Подумай, де краще зберігати стан (state). Як його краще зберігати? Чи можливо оптимізувати по пам'яті, якщо ми очікуємо, що до нас прийдуть вітатись користувачі всього Інтернету. Зроби проект на Github із репозиторієм.

Плюс, якщо є зрозумілий README, проект загорнутий у Docker, застосовані GitHub Actions, проект розгорнутий на будь-якому хостингу (heroku, digitalocean, будь-який інший)

Якщо хочеться додати щось до цього завдання - не соромся проявити творчість.


MANUAL

1) Use 'python init_db.py' to initialize DB


DOCKER COMMANDS
docker build -t evows .
docker run -p 8080:8080 -name evows-container -d evows
docker exec -it evows-container /bin/bash

docker rm evows-container

+++
docker-compose up

https://medium.com/featurepreneur/how-to-deploy-docker-container-on-heroku-part-2-eaaaf1027f0b
https://devcenter.heroku.com/articles/build-docker-images-heroku-yml

----------------------
app-name = evows

heroku login
* Login into Heroku Container
heroku container:login
* Create a new Heroku app and add the Existing local directory to Remote Heroku Repository
heroku create <app-name>
heroku git:remote -a <app-name>
* Push and Release
heroku container:push web --app <app-name>
heroku container:release web --app <app-name>
Open browser and Enter the URL https://<app-name>.herokuapp.com/

heroku open

