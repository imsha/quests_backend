from dataclasses import dataclass
from lat_lng_dto import LatLngDto


@dataclass
class PoiDto:
    id: int
    name: str
    latlng: LatLngDto
    radius: int
