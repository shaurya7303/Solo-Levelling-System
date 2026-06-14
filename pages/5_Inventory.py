import streamlit as st
from database.connection import SessionLocal
from models.achievements import InventoryItem

st.set_page_config(page_title="Inventory", page_icon="🎒", layout="wide")

db = SessionLocal()

st.title("Inventory")

items = db.query(InventoryItem).filter(InventoryItem.quantity > 0).all()

if not items:
    st.info("Your inventory is empty. Defeat bosses or earn achievements to get items.")
else:
    for item in items:
        with st.container(border=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(f"{item.name} (x{item.quantity})")
                st.write(item.description)
            with col2:
                if st.button("Use Item", key=f"use_{item.id}"):
                    # Currently dummy logic
                    item.quantity -= 1
                    db.commit()
                    st.success(f"Used {item.name}!")
                    st.rerun()

db.close()
