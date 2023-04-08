from flask import Flask
from flask import render_template
import forms
from config import Config
import gameRules
import json

app = Flask(__name__)
app.config.from_object(Config)


# функция представления
@app.route('/', methods=['POST', 'GET'])
def game():
    check_city = gameRules.Rules()
    form = forms.GameForms()
    if form.selected_city.data:  # тут мы проверяем, находится ли что-то в передаваемой форме
        if check_city.loose_win():  # проверяем достиг ли игрок одного из условий чтобы понять, игра окончена или еще нет
            check_city.current_city.append(form.selected_city.data)
            if check_city.checker(form.selected_city.data):  # проверяем, прошел ли город проверку по условиям
                a = open('guessed_cities.json', 'r')
                data = eval(a.read())
                data['cities'].append(form.selected_city.data)
                f = open('guessed_cities.json', 'w')
                f.write(json.dumps(data,
                                   ensure_ascii=False
                                   ))
                check_city.current_city = []  # верно указанный город мы записываем в файл guessed_cities в правильной форме

    return render_template('game.html',
                           form=form,
                           hp=check_city.remaining_hp,
                           scores=check_city.round,
                           message=check_city.message_for_user,
                           last_correct=check_city.last_correct[-1]
                           )
