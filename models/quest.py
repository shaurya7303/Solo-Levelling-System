from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from models.base import Base

class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    category = Column(String) # Strength, Intelligence, Discipline, Wealth, Creativity, Social
    difficulty = Column(String) # Easy, Medium, Hard, Epic, Legendary
    
    reward_xp = Column(Integer)
    reward_gold = Column(Integer)
    stat_reward = Column(Integer, default=1)
    
    penalty_xp = Column(Integer)
    penalty_gold = Column(Integer)
    
    due_date = Column(DateTime, nullable=True)
    
    completed = Column(Boolean, default=False)
    failed = Column(Boolean, default=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)

class MainQuest(Base):
    __tablename__ = "main_quests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    progress_percent = Column(Integer, default=0)
    target_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
