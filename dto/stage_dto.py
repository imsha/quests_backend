from dataclasses import dataclass
from poi_dto import PoiDto
from stage_status_dto import StageStatusDto


@dataclass
class StageDto:
    name: str
    poi: PoiDto
    status: StageStatusDto
