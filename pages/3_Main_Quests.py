import streamlit as st
from database.connection import SessionLocal
from models.quest import MainQuest

st.set_page_config(page_title="Main Quests", page_icon="🎯", layout="wide")

db = SessionLocal()

st.title("Main Quests (Long-Term Goals)")

with st.expander("Create New Main Quest"):
    with st.form("new_main_quest"):
        title = st.text_input("Title")
        desc = st.text_area("Description")
        import datetime
        target_date = st.date_input("Target Date", min_value=datetime.date.today())
        submitted = st.form_submit_button("Add Main Quest")
        
        if submitted and title:
            # target_date is a date object, we might want datetime
            dt = datetime.datetime.combine(target_date, datetime.datetime.min.time())
            mq = MainQuest(title=title, description=desc, target_date=dt)
            db.add(mq)
            db.commit()
            st.success("Main Quest Added!")
            st.rerun()

main_quests = db.query(MainQuest).all()

for mq in main_quests:
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader(mq.title)
            st.write(mq.description)
            if mq.target_date:
                st.caption(f"Target: {mq.target_date.strftime('%Y-%m-%d')}")
            st.progress(mq.progress_percent / 100.0, text=f"Progress: {mq.progress_percent}%")
        with col2:
            new_prog = st.number_input("Update Progress (%)", min_value=0, max_value=100, value=mq.progress_percent, key=f"prog_{mq.id}")
            if st.button("Update", key=f"btn_{mq.id}"):
                mq.progress_percent = new_prog
                db.commit()
                st.success("Updated!")
                st.rerun()

db.close()
