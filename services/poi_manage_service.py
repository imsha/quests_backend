from dto.poi_dto import PoiDto
from dto.lat_lng_dto import LatLngDto
from db import Session, PoiModel
from flask import request
from respect_validation import Validator
from respect_validation.Exceptions import ValidationException
from sqlalchemy import update


def validate(data: dict):
    Validator.floatVal().min(-90).max(90).claim(data['lat'])
    Validator.floatVal().min(-180).max(180).claim(data['lng'])
    Validator.stringType().length(1, 1000).claim(data['name'])
    Validator.intVal().min(1).max(1000).claim(data['radius'])


def poi_dto_from_dict(data: dict) -> PoiDto:
    latlng = LatLngDto(
        lat=data['lat'],
        lng=data['lng'],
    )
    poi_dto = PoiDto(
        id=0,
        name=data['name'],
        radius=data['radius'],
        latlng=latlng,
    )
    return poi_dto


class PoiManageService:
    def create(self, poi_dto: PoiDto) -> int:
        with Session as session:
            poi_instance = PoiModel(
                name=poi_dto.name,
                lat=poi_dto.latlng.lat,
                lng=poi_dto.latlng.lng,
                radius=poi_dto.radius,
            )
            session.add(poi_instance)
            session.commit()
            return poi_instance.id

    def update(self, poi_dto: PoiDto) -> PoiDto:
        with Session as session:
            poi = session.query(PoiModel).get(poi_dto.id)
            if not poi:
                raise ValidationException(
                    _id='poi_id',
                    input='poi_id',
                    params={
                        'poi_id': poi_dto.id
                    }
                )
            session.execute(
                update(PoiModel).where(PoiModel.id == poi_dto.id).values(
                    name=poi_dto.name,
                    lat=poi_dto.latlng.lat,
                    lng=poi_dto.latlng.lng,
                    radius=poi_dto.radius,
                )
            )
            session.commit()
            return poi_dto

    def create_from_request(self, req: request) -> PoiDto:
        data = req.json
        validate(data)
        poi_dto = poi_dto_from_dict(data)
        poi_dto.id = self.create(poi_dto=poi_dto)
        return poi_dto

    def update_from_request(self, poi_id: int, req: request) -> PoiDto:
        data = req.json
        validate(data)
        poi_dto = poi_dto_from_dict(data)
        poi_dto.id = poi_id
        return self.update(poi_dto=poi_dto)
