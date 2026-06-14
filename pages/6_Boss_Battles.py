import streamlit as st
from database.connection import SessionLocal
from services.boss_service import get_or_create_weekly_boss

st.set_page_config(page_title="Boss Battles", page_icon="🐉", layout="wide")

db = SessionLocal()

st.title("Weekly Boss Battles")

boss = get_or_create_weekly_boss(db)

if boss:
    if not boss.completed:
        st.warning(f"🚨 **ACTIVE BOSS:** {boss.title}")
        st.write(boss.description)
        st.write(f"**Goals:** {boss.goals}")
        st.write(f"**Rewards:** {boss.reward_xp} XP, {boss.reward_gold} Gold, Title: {boss.reward_title}")
        
        if st.button("Mark Boss Defeated"):
            boss.completed = True
            # In a real app, this would grant XP/Gold to the player
            db.commit()
            st.success("Boss Defeated! Rewards granted.")
            st.rerun()
    else:
        st.success(f"✅ **DEFEATED BOSS:** {boss.title}")
        st.write("You have already defeated this week's boss. Wait for the next challenge.")
else:
    st.info("No boss is currently active. The dungeon is quiet... for now. (Check back on Sunday)")

db.close()
