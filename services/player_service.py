from models.player import Player
from utils.constants import get_rank

def add_xp(db_session, player, amount):
    player.xp += amount
    while True:
        xp_required = player.level * 100
        if player.xp >= xp_required:
            player.xp -= xp_required
            player.level += 1
            player.skill_points += 1
            player.gold += 100
        else:
            break
    
    new_rank = get_rank(player.level)
    if player.rank != new_rank:
        player.rank = new_rank

def apply_quest_result(db_session, player, quest, mode_data, is_completed):
    if is_completed:
        reward_xp = int(quest.reward_xp * mode_data["reward_mult"])
        reward_gold = int(quest.reward_gold * mode_data["reward_mult"])
        add_xp(db_session, player, reward_xp)
        player.gold += reward_gold
        
        stat = quest.category.lower()
        if hasattr(player, stat):
            setattr(player, stat, getattr(player, stat) + quest.stat_reward)
        
        player.total_completed_quests += 1
        player.streak += 1
    else:
        penalty_xp = int(quest.penalty_xp * mode_data["penalty_mult"])
        penalty_gold = int(quest.penalty_gold * mode_data["penalty_mult"])
        hp_damage = mode_data["hp_damage"]

        player.xp = max(0, player.xp - penalty_xp)
        player.gold = max(0, player.gold - penalty_gold)
        player.hp = max(0, player.hp - hp_damage)
        
        player.total_failed_quests += 1
        player.streak = 0
