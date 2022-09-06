from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float, Enum, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
import enum

from config import DATABASE_URI

engine = create_engine(DATABASE_URI, echo=True, future=True)
Session = sessionmaker(engine, expire_on_commit=False)()

Base = declarative_base()


class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True)
    name = Column(String(1000))


class PoiModel(Base):
    __tablename__ = "poi"

    id = Column(Integer, primary_key=True)
    name = Column(String(1000))
    lat = Column(Float)
    lng = Column(Float)
    radius = Column(Integer)

    def __int__(self, **kwargs):
        self.name = kwargs['name']
        self.lat = kwargs['lat']
        self.lng = kwargs['lng']
        self.radius = kwargs['lng']


class StageStatus(enum.Enum):
    cancelled = -1
    new = 0
    in_process = 1
    done = 2


question_stage_table = Table(
    "question_stage",
    Base.metadata,
    Column("question_id", ForeignKey("questions.id"), primary_key=True),
    Column("stage_id", ForeignKey("stages.id"), primary_key=True),
)


class Stage(Base):
    __tablename__ = "stages"

    id = Column(Integer, primary_key=True)
    name = Column(String(1000))
    quest_id = Column(Integer)
    poi_id = Column(Integer)
    status = Column(Enum(StageStatus))
    started = Column(DateTime, nullable=True)
    done = Column(DateTime, nullable=True)
    cancelled = Column(DateTime, nullable=True)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    text = Column(String(1000))


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True)
    message = Column(String(1000))


Base.metadata.create_all(engine)
