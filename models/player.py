from sqlalchemy import Column, Integer, String, Float, Boolean
from models.base import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="Sung Jinwoo")
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    gold = Column(Integer, default=0)
    hp = Column(Integer, default=100)
    rank = Column(String, default="E")
    streak = Column(Integer, default=0)

    # Stats
    strength = Column(Integer, default=10)
    intelligence = Column(Integer, default=10)
    discipline = Column(Integer, default=10)
    wealth = Column(Integer, default=10)
    creativity = Column(Integer, default=10)
    social = Column(Integer, default=10)

    skill_points = Column(Integer, default=0)

    # Difficulty Mode: Casual, Normal, Hard, Brutal, Monarch
    mode = Column(String, default="Normal")

    total_completed_quests = Column(Integer, default=0)
    total_failed_quests = Column(Integer, default=0)

class Title(Base):
    __tablename__ = "titles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    unlocked = Column(Boolean, default=False)
    equipped = Column(Boolean, default=False)

class Settings(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    ollama_model = Column(String, default="llama3")
    theme = Column(String, default="dark")
    daily_xp_multiplier = Column(Float, default=1.0)
