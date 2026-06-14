import streamlit as st
from database.connection import SessionLocal
from models.player import Player, Settings
from models.quest import Quest
from services.ai_service import DungeonMaster
from datetime import datetime

st.set_page_config(page_title="Dungeon Master", page_icon="🧙‍♂️", layout="wide")

db = SessionLocal()
player = db.query(Player).first()
settings = db.query(Settings).first()

st.title("Dungeon Master AI")
st.write(f"Connected to Model: **{settings.ollama_model}**")

dm = DungeonMaster(model_name=settings.ollama_model)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Morning Briefing")
    if st.button("Generate Morning Briefing"):
        with st.spinner("DM is thinking..."):
            active_quests = db.query(Quest).filter(Quest.completed == False, Quest.failed == False).all()
            briefing = dm.morning_briefing(player.name, player.level, active_quests)
            st.info(briefing)

with col2:
    st.subheader("Night Report")
    if st.button("Generate Night Report"):
        with st.spinner("DM is reviewing your day..."):
            today = datetime.utcnow().date()
            # Simplistic check for today's completed/failed
            completed = db.query(Quest).filter(Quest.completed == True).count()
            failed = db.query(Quest).filter(Quest.failed == True).count()
            report = dm.night_report(player.name, completed, failed)
            st.warning(report)

st.markdown("---")
st.subheader("Quest Suggestions")
if st.button("Ask for Suggestions"):
    with st.spinner("Analyzing stats..."):
        stats = f"STR: {player.strength}, INT: {player.intelligence}, DIS: {player.discipline}, WEA: {player.wealth}, CRE: {player.creativity}, SOC: {player.social}"
        suggestions = dm.quest_suggestions(stats)
        st.success(suggestions)

db.close()
