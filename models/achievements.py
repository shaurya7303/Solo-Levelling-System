from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from models.base import Base

class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    reward_xp = Column(Integer, default=0)
    reward_gold = Column(Integer, default=0)
    reward_title = Column(String, nullable=True)
    unlocked = Column(Boolean, default=False)
    unlocked_at = Column(DateTime, nullable=True)

class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    item_type = Column(String) # Scroll, Potion, Token
    quantity = Column(Integer, default=0)
    description = Column(String)

class BossBattle(Base):
    __tablename__ = "boss_battles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    goals = Column(String) # JSON string of goals
    reward_xp = Column(Integer)
    reward_gold = Column(Integer)
    reward_title = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
