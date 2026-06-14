from datetime import datetime
from models.quest import Quest
from services.player_service import apply_quest_result
from utils.constants import DIFFICULTY_MODES

def complete_quest(db_session, player, quest):
    if quest.completed or quest.failed:
        return
    
    quest.completed = True
    quest.completed_at = datetime.utcnow()
    
    mode_data = DIFFICULTY_MODES.get(player.mode, DIFFICULTY_MODES["Normal"])
    apply_quest_result(db_session, player, quest, mode_data, is_completed=True)
    
    db_session.commit()

def fail_quest(db_session, player, quest):
    if quest.completed or quest.failed:
        return
    
    quest.failed = True
    
    mode_data = DIFFICULTY_MODES.get(player.mode, DIFFICULTY_MODES["Normal"])
    apply_quest_result(db_session, player, quest, mode_data, is_completed=False)
    
    db_session.commit()
