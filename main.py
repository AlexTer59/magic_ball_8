import random


def choice(choise_answers):
    return choise_answers[random.randint(0, len(choise_answers))]


def is_valid(answer):
    if answer == 'y' or answer == 'n':
        if answer == 'n':
            global is_one_more
            is_one_more = False
    else:
        print("А может быть все-таки введем Y или N:")
        answer = input()
        is_valid(answer)


answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
print("Как вас зовут?")
user_name = input()
print("Привет,", user_name)
is_one_more = True
while is_one_more:
    print("Введите ваш вопрос:")
    question = input()
    print(choice(answers))
    print("Хотите задать еще вопрос Y/N?")
    is_valid(input().lower())
print("Возвращайся, если возникнут вопросы!")
