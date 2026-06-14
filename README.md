# Solo Leveling System

A complete, local-first RPG productivity system inspired by *Solo Leveling*. The system transforms your real-life tasks into quests, tracking your progression through levels, stats, and achievements, all while an AI "Dungeon Master" provides narrative feedback and suggestions.

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
git clone https://github.com/yourusername/solo-leveling-system.git
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
