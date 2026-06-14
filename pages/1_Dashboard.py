import streamlit as st
import plotly.graph_objects as go
from database.connection import SessionLocal
from models.player import Player
from models.quest import Quest

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

db = SessionLocal()
player = db.query(Player).first()

st.title("Player Dashboard")

# Player Card
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown(f"### {player.name}")
    st.markdown(f"**Level:** {player.level}")
    st.markdown(f"**Rank:** {player.rank}")
    st.markdown(f"**Mode:** {player.mode}")
    st.markdown(f"**Streak:** {player.streak} days")
with col2:
    xp_req = player.level * 100
    xp_req = xp_req if xp_req > 0 else 100
    st.progress(player.xp / xp_req if player.xp <= xp_req else 1.0, text=f"XP: {player.xp}/{xp_req}")
    st.progress(player.hp / 100.0 if player.hp <= 100 else 1.0, text=f"HP: {player.hp}/100")
    st.markdown(f"**Gold:** {player.gold} 🪙")

st.markdown("---")

# Stats Radar Chart or Bars
st.subheader("Attributes")
col_s1, col_s2, col_s3, col_s4, col_s5, col_s6 = st.columns(6)
col_s1.metric("Strength", player.strength)
col_s2.metric("Intelligence", player.intelligence)
col_s3.metric("Discipline", player.discipline)
col_s4.metric("Wealth", player.wealth)
col_s5.metric("Creativity", player.creativity)
col_s6.metric("Social", player.social)

st.markdown("---")
# Active Quests Summary
st.subheader("Active Quests")
active_quests = db.query(Quest).filter(Quest.completed == False, Quest.failed == False).all()
if active_quests:
    for q in active_quests:
        st.write(f"- **{q.title}** [{q.difficulty}] ({q.category})")
else:
    st.write("No active quests. Go to Quests to add some!")

db.close()
