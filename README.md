# FUCK Russian Chanel

Невеличкий скрипт, який дозволяє автоматизувати рейсові маршрути ~~россійського військового корабля~~ деяких надто токсичних telegram каналів

## Підготовка 
### Локально: 
1. Встановіть Python останньої версії (не нижче 3.7)
2. Скопіюйте скрипт собі локально (git clone https://github.com/torvald2/fuckrussianchannel.git)
3. Бажано створити у каталозі віртуальне середовище 
   

    > python3 -m virtualenv venv  

Та активувати його 
   Mac або linux: 
   

    source venv/bin/activate
Windows
 

     venv\Scripts\activate.bat

4. Встановити залежності:

    > pip install -r requirements.txt
5. Заходемо ,https://my.telegram.org, логінимось та беремо звідти app_id та app_hash. Прописуємо у відповідні строки файлу config.ini
6. Параметр join_period конфіг файлу регулює через який проміжок часу у секундах після приєднання до каналу буде відправлена скарга та відбудеться відьеднання від каналу

## Docker 
Конфігурування через config.ini не потрібне. У разі використання докеру конфіг береться з environ variables
   

    > docker build -t reporter .

## Використання
## Локально 
Список каналів які блокуються береться з вебу (https://raw.githubusercontent.com/torvald2/fuckrussianchannel/master/chanels.json). 
Якщо потрібно використати локальний файл то вкажіть у config.ini report_store= local
Список текстів скарг у messages.json - я не планую добавляти на сервак. Кожен може доповнювати своїми 

Запуск: 

    python main.py

При першому запуску запитають телефон та код підтверждення. Далі ліба создасть файл сессії і наступні рази питати не буде
На кожен заблочений канал буде дебаг месседж.
## Docker
Для запуску
    docker run -ti -e API_ID=[Ваш app_id] -e API_HASH=[Ваш  api hash] reporter

Також можна вказувати такі змінні оточення:
- JOIN_PERIOD - період перебування на каналі 15 сек за замовчанням
- REPORT_STORE - звідки брати перелік каналів (за замовченням web, можна вказати local для використання локального файлу)
- 

Побажання та пропозиції @torvald2