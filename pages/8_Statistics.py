import streamlit as st
import plotly.express as px
import pandas as pd
from database.connection import SessionLocal
from models.player import Player
from models.quest import Quest

st.set_page_config(page_title="Statistics", page_icon="📈", layout="wide")

db = SessionLocal()
player = db.query(Player).first()

st.title("Player Statistics")

# Basic stats from player
col1, col2 = st.columns(2)
col1.metric("Total Quests Completed", player.total_completed_quests)
col2.metric("Total Quests Failed", player.total_failed_quests)

# Charts
st.subheader("Quest Category Breakdown")
quests = db.query(Quest).all()
if quests:
    df = pd.DataFrame([{
        "title": q.title, 
        "category": q.category, 
        "status": "Completed" if q.completed else "Failed" if q.failed else "Active"
    } for q in quests])
    
    # Pie chart for categories
    fig1 = px.pie(df, names='category', title='Quests by Category')
    st.plotly_chart(fig1)
    
    # Bar chart for completion status
    status_counts = df['status'].value_counts().reset_index()
    status_counts.columns = ['status', 'count']
    fig2 = px.bar(status_counts, x='status', y='count', title='Quest Status Distribution', color='status')
    st.plotly_chart(fig2)
else:
    st.info("No data available yet. Complete some quests!")

db.close()
