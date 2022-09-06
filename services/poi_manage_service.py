from dto.poi_dto import PoiDto
from dto.lat_lng_dto import LatLngDto
from db import Session, PoiModel
from flask import request
from respect_validation import Validator as v


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

    def create_from_request(self, req: request):
        data = req.json

        v.floatVal().min(-90).max(90).claim(data['lat'])
        v.floatVal().min(-180).max(180).claim(data['lng'])
        v.stringType().length(1, 1000).claim(data['name'])
        v.intVal().min(1).max(1000).claim(data['radius'])

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

        poi_dto.id = self.create(poi_dto=poi_dto)

        return poi_dto.__dict__
