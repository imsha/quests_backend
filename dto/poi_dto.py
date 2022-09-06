from dataclasses import dataclass
from dto.lat_lng_dto import LatLngDto

from dto.base_dto import BaseDto


@dataclass
class PoiDto(BaseDto):
    id: int
    name: str
    latlng: LatLngDto
    radius: int
