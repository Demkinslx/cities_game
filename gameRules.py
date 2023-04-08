import json


class Rules:
    remaining_hp = 10
    message_for_user = 'Ну что ж, приступим'
    round = 1
    current_city = []
    last_correct = ['']
    with open('guessed_cities.json', 'w') as file:
        dict_sities = {"cities": []}
        json_cities = json.dumps(dict_sities)
        file.write(json_cities)

    # создаем условия для проигрыша, либо выигрыша
    def loose_win(self):
        check_result = [Rules.remaining_hp == 0, Rules.round == 100]
        if check_result[0]:
            Rules.message_for_user = 'Игра окончена,вы проиграли'
            return False
        elif not check_result[0] and check_result[1]:
            Rules.message_for_user = 'Поздравляем, вы победили'
            return False
        else:
            return True

    # проверяем есть ли введеный игроком город в базе
    def if_city(self, user_city):
        with open('only_cities.json', 'r', encoding='utf-8') as file:
            data = eval(file.read())
            if str(user_city) in data:
                return True
            else:
                Rules.message_for_user = "Такого города в России не существует(("
                return False

    # проверяем, не вводил ли игрок этот город ранее
    def if_used(self, this_word):
        with open('guessed_cities.json', 'r') as file:
            data: list = eval(file.read())
            if str(this_word) not in data['cities']:
                return True
            else:
                Rules.message_for_user = "Такой город вы уже угадывали"
                return False

    # проверяем, сходится ли последняя буква предыдущего города и первая буква введенного игроком города
    def if_last_letter(self, this_word):
        a = open('guessed_cities.json', 'r')
        data = json.load(a)['cities']
        a.seek(0)
        if Rules.round > 1:
            nado = Rules.current_city[-1][0].lower()
            last_letter = data[-1][-1]
            print(nado)
            print(last_letter)
            if last_letter in ['ь', 'й', 'ъ', 'ё', 'ы']:
                counter = -1
                while last_letter in ['ь', 'й', 'ъ', 'ё', 'ы']:
                    last_letter = data[-1][counter]
                    if last_letter not in ['ь', 'й', 'ъ', 'ё', 'ы']:
                        break
                    else:
                        counter -= 1
            if last_letter.lower() == nado:
                Rules.current_city = []
                return True
            else:
                Rules.current_city = []
                Rules.message_for_user = "Название города не начинается на последнюю букву предыдущего"
                return False
        else:
            return True

    # а здесь мы проверяем результат всех функций, соответственно если введенный игроком город прошел проверку в трех функциях, мы возвращаем true
    def checker(self, city_name):
        results = [self.if_used(city_name), self.if_city(city_name),
                   self.if_last_letter(city_name)]
        if all(results):
            Rules.round += 1
            Rules.message_for_user = 'Хороший город, продолжаем'
            Rules.last_correct.append(city_name)
            return True
        else:
            Rules.round += 1
            Rules.remaining_hp -= 1
            return False
