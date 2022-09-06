from flask import Flask, jsonify, request
from services.quest_service import QuestService

app = Flask(__name__)

if __name__ == "__main__":
    app.run()


@app.get("/quests")
def quest_list_action():
    return QuestService().get_all()


# todo разобраться как выводить 404 ошибку
@app.get("/quests/<int:quest_id>")
def quest_view_action(quest_id: int):
    return QuestService().get_one(quest_id)


@app.post("/poi")
def poi_create_action():
    return {
        'success': True
    }


@app.post("/stage")
def state_create_action():
    return {
        'success': True
    }

# todo логика poi в простом варианте
#       широта, долгота, радиус
#       название

# todo логика квеста
#       один-ко-многим poi, порядковый номер прохождения, идентификатор не зависящий от порядкового номера
#       связь квест-poi-вопросы. На одной точке может быть много вопросов.
#       признак, пройдена ли точка

# todo логика прохождения квеста
#       связь юзера с квестом
#       даты начала, завершения, отмены
#       статус


# todo сделать реляцию вопросов и ответов
# todo сделай запись координат
# todo сделай логику запуска квеста, отмены и постановки на паузу
# todo разберись как динамически трансформировать данные из базы в json
