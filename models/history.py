from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from models.base import Base

class DailyHistory(Base):
    __tablename__ = "daily_history"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow, index=True)
    level = Column(Integer)
    xp = Column(Integer)
    quests_completed = Column(Integer, default=0)
    streak = Column(Integer, default=0)
