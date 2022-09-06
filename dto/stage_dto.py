from dataclasses import dataclass

from dto.base_dto import BaseDto


@dataclass
class StageDto(BaseDto):
    id: int
    name: str
    quest_id: int
    poi_id: int
    author_id: int
    sort: int
