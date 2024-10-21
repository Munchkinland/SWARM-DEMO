# handoff_functions.py
class HandoffManager:
    def __init__(self):
        self.handoffs = []

    def add_handoff(self, topic, expert):
        self.handoffs.append((topic, expert))

    def list_handoffs(self):
        return [f"Handoff Topic: {topic}, Expert: {expert}" for topic, expert in self.handoffs]

class HandoffLogger:
    def log(self, message):
        print(f"Log: {message}")

    def log_handoff(self, topic, expert):
        self.log(f"Handoff made for topic '{topic}' to expert '{expert}'.")
