from db import Quest
from db import Session


class QuestService:

    def get_all(self):
        with Session as session:
            result = []
            for it in session.query(Quest).all():
                result.append({
                    'id': it.id,
                    'name': it.name,
                })
            return result

    def get_one(self, quest_id: int):
        with Session as session:
            it = session.query(Quest).get(quest_id)
            return {
                'id': it.id,
                'name': it.name,
            }
