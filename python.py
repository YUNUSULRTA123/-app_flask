from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return f'''
    <h1>HELLO GUYS!!!!!</h1>
    <a href="/randomfact">Посмотреть случайный факт!</a>    
    <a href="/passwordgenerator">Случайный пароль!</a>
    '''
@app.route("/randomfact")
def facts():
    facts_list = [
        "Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
        "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.",
        "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
        "Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.",
        "Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.",
        "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.",
        "Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.",
        "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ."
    ]
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/passwordgenerator")
def rand_pass():
    password="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password_real=""
    for i in range(int(random.choice(1,20))):
        password_real+=random.choice(password)
        return f'''
        <h1>{password_real}</h1>
        '''
@app.route("/orelilireshka")
def brosok_monetki():
    Orel_ili_reshka=random.choice(1,2)
    if Orel_ili_reshka == 1:
        return f'''
<p>ВАМ ВЫПАЛ ОРЁЛ</p>
'''
    elif Orel_ili_reshka == 2:
        return f'''
<p>ВАМ ВЫПАЛА РЕШКА</p>
'''
app.run(debug=True)
