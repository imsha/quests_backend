from flask import Flask, request
from services.quest_service import QuestService
from services.poi_manage_service import PoiManageService
from services.stage_manage_service import StageManageService

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
    return PoiManageService().create_from_request(request).to_dict()


@app.put("/poi/<int:poi_id>")
def poi_update_action(poi_id: int):
    return PoiManageService().update_from_request(poi_id, request).to_dict()


@app.post("/stage")
def state_create_action():
    return StageManageService().create_from_request(request).to_dict()


@app.delete("/stage/<int:stage_id>")
def state_create_action():
    # todo если уже выполняются квесты, то помечай удаленным, если квестов не было, то удаляй из базы запись
    return [123]

# todo Дальше сделай создание вопросов и ответов и привязку, затем привязку их к stage

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
