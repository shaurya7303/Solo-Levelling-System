# Solo Leveling System


<img width="860" height="486" alt="wp13812155" src="https://github.com/user-attachments/assets/256f9bdd-022b-4644-9138-50e173645559" />

A complete, local-first RPG productivity system inspired by *Solo Leveling*. The system transforms your real-life tasks into quests, tracking your progression through levels, stats, and achievements, all while an AI "Dungeon Master" provides narrative feedback and suggestions.

<img width="899" height="500" alt="solo-leveling-lord-big-smile-f3jx1bbid7x1gq1u (1)" src="https://github.com/user-attachments/assets/67ea73e4-3fdd-4b49-8e3e-a027903cf60c" />


## Features

- **RPG Mechanics:** Complete quests to earn XP, Gold, and improve 6 core stats (Strength, Intelligence, Discipline, Wealth, Creativity, Social).
- **Difficulty Modes:** Choose your path from Casual (no penalties) to Monarch (extreme penalties for failure, high rewards). Failing quests damages your HP.
- **Quest Management:** Create daily tasks (Quests) and long-term goals (Main Quests).
- **Achievements & Titles:** Unlock achievements for reaching milestones and equip titles like "Shadow Monarch" or "Elite Hunter".
- **Weekly Boss Battles:** Face auto-generated challenges every Sunday for massive rewards.
- **Statistics Dashboard:** Visualize your quest completion rates and attribute growth with interactive Plotly charts.
- **AI Dungeon Master:** Fully integrated with local **Ollama** models. The system generates dark, RPG-style morning briefings, night reports, and quest suggestions based on your weakest stats.
- **Local-First & Private:** Everything is stored locally in an SQLite database. No cloud services or internet connection required (except to download AI models).

## Tech Stack

- **Frontend:** Streamlit
- **Backend/Logic:** Python 3.12
- **Database:** SQLite & SQLAlchemy ORM
- **Data Visualization:** Plotly & Pandas
- **AI Engine:** Ollama

## Installation

### 1. Prerequisites
- Python 3.12+ installed.
- [Ollama](https://ollama.com/) installed for the local AI Dungeon Master features.

### 2. Setup the Repository
Clone the repository and navigate into the project directory:
```bash
git clone https://github.com/shaurya7303/Solo-Levelling-System)
cd solo-leveling-system
```

### 3. Install Dependencies
It is recommended to use a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 4. Setup Ollama
The AI services rely on Ollama running in the background. The default model is set to `llama3.2:1b`. Pull the model using:
```bash
ollama pull llama3.2:1b
```
*(You can also pull and use other models like `mistral` or `qwen3` and change them in the Settings page).*

### 5. Run the Application
Launch the Streamlit app:
```bash
streamlit run app.py
```
The application will automatically initialize the database, create your default "Sung Jinwoo" player profile, and open the dashboard in your web browser.

## Project Structure

```
├── app.py                  # Main Streamlit entry point & DB initialization
├── requirements.txt        # Python dependencies
├── database/               # SQLite connection setup
├── models/                 # SQLAlchemy schemas (Player, Quest, Achievements, etc.)
├── services/               # Business logic (Leveling, Bosses, AI interaction)
├── utils/                  # Constants and game matrices
└── pages/                  # Streamlit multi-page UI views
    ├── 1_Dashboard.py
    ├── 2_Quests.py
    ├── 3_Main_Quests.py
    ├── 4_Achievements.py
    ├── 5_Inventory.py
    ├── 6_Boss_Battles.py
    ├── 7_Dungeon_Master.py
    ├── 8_Statistics.py
    └── 9_Settings.py
```

## License

This project is open-source and available for personal use. Arise!

https://github.com/user-attachments/assets/64bb4123-e4c2-42c9-9d07-5ab4a2a9e702

