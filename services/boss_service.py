from datetime import datetime
from models.achievements import BossBattle

def get_or_create_weekly_boss(db_session):
    today = datetime.utcnow()
    # Check if Sunday (weekday() == 6)
    if today.weekday() != 6:
        return None
        
    start_of_week = today.replace(hour=0, minute=0, second=0, microsecond=0)
    existing_boss = db_session.query(BossBattle).filter(BossBattle.created_at >= start_of_week).first()
    
    if existing_boss:
        return existing_boss
        
    new_boss = BossBattle(
        title=f"Weekly Boss Challenge - Week {today.isocalendar()[1]}",
        description="Defeat the weekly boss by completing these goals.",
        goals="10 quests, 10 hours study, 3 workouts",
        reward_xp=1000,
        reward_gold=500,
        reward_title="Boss Slayer"
    )
    db_session.add(new_boss)
    db_session.commit()
    db_session.refresh(new_boss)
    return new_boss
