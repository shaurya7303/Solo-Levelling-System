DIFFICULTY_REWARDS = {
    "Easy": {"xp": 25, "gold": 10},
    "Medium": {"xp": 50, "gold": 25},
    "Hard": {"xp": 100, "gold": 50},
    "Epic": {"xp": 250, "gold": 100},
    "Legendary": {"xp": 500, "gold": 250}
}

DIFFICULTY_MODES = {
    "Casual": {"reward_mult": 1.0, "penalty_mult": 0.0, "hp_damage": 0},
    "Normal": {"reward_mult": 1.0, "penalty_mult": 1.0, "hp_damage": 5},
    "Hard": {"reward_mult": 1.2, "penalty_mult": 1.0, "hp_damage": 10},
    "Brutal": {"reward_mult": 1.5, "penalty_mult": 1.5, "hp_damage": 20},
    "Monarch": {"reward_mult": 2.0, "penalty_mult": 2.0, "hp_damage": 30}
}

def get_rank(level):
    if level <= 10: return "E"
    elif level <= 20: return "D"
    elif level <= 35: return "C"
    elif level <= 50: return "B"
    elif level <= 70: return "A"
    elif level <= 90: return "S"
    elif level <= 120: return "SS"
    else: return "MONARCH"
