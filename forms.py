from wtforms import StringField
from wtforms import SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


# создаем класс с двумя формами - поля для ввода названия города и кнопку подтверждения
class GameForms(FlaskForm):
    selected_city = StringField('Введите название города', validators=[DataRequired()])
    submit_city = SubmitField('Подтвердить')
