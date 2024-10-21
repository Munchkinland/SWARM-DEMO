# agents/game_master.py
from swarm import Agent

class GameMaster(Agent):
    def __init__(self):
        super().__init__(
            name="Game Master",
            instructions="You are the game master for a language learning idiom game. Introduce the game, explain rules, and coordinate between players and language experts."
        )
    
    def introduce_game(self):
        return "Welcome to the language learning idiom game Swarm Demo! You will learn idioms in English and Spanish, Let's get started!"
    
    def explain_rules(self):
        return "You will ask for explanations of idioms, and I will coordinate with language experts to provide you the best insights."
