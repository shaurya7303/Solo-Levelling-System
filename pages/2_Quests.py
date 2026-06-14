import streamlit as st
from database.connection import SessionLocal
from models.quest import Quest
from models.player import Player
from services.quest_service import complete_quest, fail_quest

st.set_page_config(page_title="Quests", page_icon="📜", layout="wide")

db = SessionLocal()
player = db.query(Player).first()

st.title("Quest Board")

with st.expander("Create New Quest"):
    with st.form("new_quest_form"):
        title = st.text_input("Title")
        desc = st.text_area("Description")
        col1, col2 = st.columns(2)
        category = col1.selectbox("Category", ["Strength", "Intelligence", "Discipline", "Wealth", "Creativity", "Social"])
        difficulty = col2.selectbox("Difficulty", ["Easy", "Medium", "Hard", "Epic", "Legendary"])
        
        # We can dynamically get rewards based on difficulty, but for UI simplicity, we use constants or manual
        st.write("Rewards are auto-calculated based on difficulty mode.")
        submitted = st.form_submit_button("Add Quest")
        
        if submitted and title:
            # Quick lookup for base rewards
            from utils.constants import DIFFICULTY_REWARDS
            base_reward = DIFFICULTY_REWARDS[difficulty]
            
            new_q = Quest(
                title=title,
                description=desc,
                category=category,
                difficulty=difficulty,
                reward_xp=base_reward["xp"],
                reward_gold=base_reward["gold"],
                penalty_xp=int(base_reward["xp"] / 2),
                penalty_gold=int(base_reward["gold"] / 2)
            )
            db.add(new_q)
            db.commit()
            st.success("Quest Added!")
            st.rerun()

st.subheader("Active Quests")
active_quests = db.query(Quest).filter(Quest.completed == False, Quest.failed == False).all()

for q in active_quests:
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{q.title}** | {q.category} | {q.difficulty}")
            st.write(q.description)
            st.caption(f"Rewards: {q.reward_xp} XP, {q.reward_gold} Gold")
        with col2:
            if st.button("Complete", key=f"comp_{q.id}", type="primary"):
                complete_quest(db, player, q)
                st.success("Quest Completed!")
                st.rerun()
            if st.button("Fail", key=f"fail_{q.id}"):
                fail_quest(db, player, q)
                st.error("Quest Failed.")
                st.rerun()

st.subheader("Completed Quests")
completed_quests = db.query(Quest).filter(Quest.completed == True).order_by(Quest.completed_at.desc()).limit(10).all()
for q in completed_quests:
    st.write(f"- {q.title} ({q.difficulty}) - Completed at {q.completed_at}")

db.close()
