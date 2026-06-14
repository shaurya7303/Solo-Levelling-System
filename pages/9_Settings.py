import streamlit as st
from database.connection import SessionLocal
from models.player import Player, Settings
import pandas as pd
from models.quest import Quest

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="wide")

db = SessionLocal()
player = db.query(Player).first()
settings = db.query(Settings).first()

st.title("Settings")

with st.expander("Player Settings", expanded=True):
    new_name = st.text_input("Player Name", player.name)
    mode_options = ["Casual", "Normal", "Hard", "Brutal", "Monarch"]
    try:
        current_idx = mode_options.index(player.mode)
    except ValueError:
        current_idx = 1
    mode = st.selectbox("Difficulty Mode", mode_options, index=current_idx)
    
    if st.button("Save Player Settings"):
        player.name = new_name
        player.mode = mode
        db.commit()
        st.success("Player settings saved!")

with st.expander("System Settings"):
    model_options = ["llama3", "mistral", "qwen3", "gemma3", "qwen2.5"]
    try:
        current_m_idx = model_options.index(settings.ollama_model)
    except ValueError:
        current_m_idx = 0
    model = st.selectbox("Ollama Model", model_options, index=current_m_idx)
    
    if st.button("Save System Settings"):
        settings.ollama_model = model
        db.commit()
        st.success("System settings saved!")

with st.expander("Data Management"):
    st.write("Export your data to CSV")
    
    quests = db.query(Quest).all()
    if quests:
        df = pd.DataFrame([q.__dict__ for q in quests])
        # Drop sqlalchemy instance state
        if '_sa_instance_state' in df.columns:
            df = df.drop(columns=['_sa_instance_state'])
            
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Quests CSV",
            data=csv,
            file_name='solo_leveling_quests.csv',
            mime='text/csv',
        )
    else:
        st.info("No quest data to export.")

db.close()
