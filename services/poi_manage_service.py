from dto.poi_dto import PoiDto
from db import Session, PoiModel


class PoiManageService:
    def create(self, poi_dto: PoiDto):
        with Session as session:
            poi_instance = PoiModel(
                name=poi_dto.name,
                lat=poi_dto.latlng.lat,
                lng=poi_dto.latlng.lng,
                radius=poi_dto.radius,
            )
            session.add(poi_instance)
            session.commit()
