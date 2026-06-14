import streamlit as st
from database.connection import engine, SessionLocal
from models.base import Base
from models.player import Player, Settings

# Initialize database
def init_db():
    # Import all models here to ensure they are registered with Base
    import models.player
    import models.quest
    import models.history
    import models.achievements

    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Create default player if not exists
    player = db.query(Player).first()
    if not player:
        player = Player(name="Sung Jinwoo")
        db.add(player)
        db.commit()
    
    # Create default settings if not exists
    settings = db.query(Settings).first()
    if not settings:
        settings = Settings()
        db.add(settings)
        db.commit()
        
    db.close()

# Page Config
st.set_page_config(
    page_title="Solo Leveling System",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize on run
init_db()

st.title("Solo Leveling System")
st.write("Welcome, Player.")
st.write("Please use the sidebar to navigate to your Dashboard, Quests, and other sections.")

if st.button("Arise"):
    st.toast("Welcome to the system.", icon="🗡️")
