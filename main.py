                                #main.py
from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/https://www.youtube.com/watch?v=xTYck8mPwOI')

@app.route('/random_fact')
def random_fact():
    facts_list=["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
                "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
                "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.",
                "Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.",
                "Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.",
                "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.",
                "Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.",
                "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ."
    ]
    return f'<p>{random.choice(facts_list)}</p>'




app.run(debug = True)
                                #index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>Hello world!</p>
    <a href="/random_fact">Посмотреть случайный факт!</a>
    
    <A href="https://www.youtube.com/watch?v=xTYck8mPwOI">а тут я просто долго проходил карту по роблокс лол</A>
</body>
</html>
