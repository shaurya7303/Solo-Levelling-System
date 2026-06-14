import streamlit as st
from database.connection import SessionLocal
from models.player import Player, Title
from models.achievements import Achievement

st.set_page_config(page_title="Achievements & Titles", page_icon="🏆", layout="wide")

db = SessionLocal()
player = db.query(Player).first()

st.title("Achievements & Titles")

st.subheader("Titles")
titles = db.query(Title).all()

if not titles:
    st.info("No titles discovered yet. Keep leveling up!")
else:
    for t in titles:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{t.name}** {'(Equipped)' if t.equipped else ''}")
        with col2:
            if t.unlocked and not t.equipped:
                if st.button("Equip", key=f"equip_{t.id}"):
                    # Unequip others
                    db.query(Title).update({Title.equipped: False})
                    t.equipped = True
                    db.commit()
                    st.success(f"Equipped {t.name}!")
                    st.rerun()

st.markdown("---")
st.subheader("Achievements")
achievements = db.query(Achievement).all()

if not achievements:
    st.info("Complete quests to unlock achievements!")
else:
    for a in achievements:
        if a.unlocked:
            st.success(f"🔓 **{a.name}** - {a.description}")
        else:
            st.error(f"🔒 **{a.name}** - {a.description}")

db.close()
