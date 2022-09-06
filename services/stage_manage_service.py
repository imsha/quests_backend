from dto.stage_dto import StageDto
from respect_validation import Validator
from flask import request
from db import Session, StateModel


def validate(data: dict):
    Validator.stringType().length(1, 1000).claim(data['name'])
    # todo проверяй автора квеста
    Validator.intVal().claim(data['quest_id'])
    # todo проверяй чтобы одна точка не была подряд
    Validator.intVal().claim(data['poi_id'])
    Validator.intVal().min(-1000).max(1000).claim(data['sort'])


def stage_dto_from_dict(data: dict) -> StageDto:
    stage_dto = StageDto(
        id=0,
        name=data['name'],
        quest_id=data['quest_id'],
        poi_id=data['poi_id'],
        author_id=0,
    )
    return stage_dto


class StageManageService:

    def create(self, stage_dto: StageDto):
        with Session as session:
            stage_instance = StateModel(
                name=stage_dto.name,
                quest_id=stage_dto.quest_id,
                poi_id=stage_dto.poi_id,
                author_id=stage_dto.author_id,
                sort=stage_dto.sort,
            )
            session.add(stage_instance)
            session.commit()
            return stage_instance.id

    def create_from_request(self, req: request) -> StageDto:
        data = req.json
        validate(data)
        stage_dto = stage_dto_from_dict(data)

        # todo пробрось в авторы текущего юзера
        stage_dto.author_id = 123
        stage_dto.id = self.create(stage_dto=stage_dto)
        return stage_dto
