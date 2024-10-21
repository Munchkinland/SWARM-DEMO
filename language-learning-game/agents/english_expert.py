# agents/english_expert.py
from swarm import Agent
from pydantic import Field, BaseModel
from typing import Dict

class EnglishExpert(Agent):
    known_idioms: Dict[str, str] = Field(default_factory=lambda: {
        "break the ice": "To initiate conversation in a social setting.",
        "hit the nail on the head": "To be exactly correct about something.",
        "spill the beans": "To reveal a secret."
    })

    def __init__(self):
        super().__init__(
            name="English Expert",
            instructions="You are an expert in English idioms. Provide explanations and context for idioms when asked."
        )
    
    def can_help_with(self, idiom: str) -> bool:
        """Check if the expert can help with the given idiom."""
        return idiom in self.known_idioms

    def explain_idiom(self, idiom: str) -> str:
        """Provide an explanation for the given idiom."""
        if idiom in self.known_idioms:
            explanation = self.known_idioms[idiom]
            return f"The idiom '{idiom}' means: {explanation}"
        else:
            return f"Sorry, I do not have an explanation for the idiom '{idiom}'."
