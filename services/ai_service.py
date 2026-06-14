import requests
import json

class DungeonMaster:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name
        self.api_url = "http://localhost:11434/api/generate"

    def _generate(self, prompt):
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }
        try:
            response = requests.post(self.api_url, json=payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "No response from DM.")
        except Exception as e:
            return f"[DM Communication Error]: Ensure Ollama is running with the model '{self.model_name}'. Error details: {str(e)}"

    def morning_briefing(self, player_name, level, quests):
        prompt = f"Act as the system from Solo Leveling. The player {player_name} is Level {level}. They have {len(quests)} active quests today. Write a short, motivating morning briefing in a dark, serious RPG tone."
        return self._generate(prompt)

    def night_report(self, player_name, completed_count, failed_count):
        prompt = f"Act as the system from Solo Leveling. The player {player_name} completed {completed_count} quests and failed {failed_count} quests today. Write a brief night report summarizing their performance. Tone: objective, slightly ominous."
        return self._generate(prompt)

    def quest_suggestions(self, stats_summary):
        prompt = f"Act as the system from Solo Leveling. Given the player's stats: {stats_summary}. Suggest 3 short, actionable real-life quests they can do to improve their lowest stats."
        return self._generate(prompt)

    def generate_lore(self, player_name, event):
        prompt = f"Act as the system from Solo Leveling. The player {player_name} just achieved: '{event}'. Write a 3-sentence lore popup describing this."
        return self._generate(prompt)
