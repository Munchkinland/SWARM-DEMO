# agents/spanish_expert.py
from swarm import Agent
from pydantic import Field
from typing import Dict

class SpanishExpert(Agent):
    known_idioms: Dict[str, str] = Field(default_factory=lambda: {
        "dar en el clavo": "To hit the nail on the head.",
        "romper el hielo": "To break the ice.",
        "tirar la toalla": "To throw in the towel."
    })

    def __init__(self):
        super().__init__(
            name="Spanish Expert",
            instructions="You are an expert in Spanish idioms. Provide explanations and context for idioms when asked."
        )

    def can_help_with(self, idiom: str) -> bool:
        """Check if the expert can help with the given idiom."""
        return idiom in self.known_idioms

    def explain_idiom(self, idiom: str) -> str:
        """Provide an explanation for the given idiom."""
        if idiom in self.known_idioms:
            explanation = self.known_idioms[idiom]
            return f"El modismo '{idiom}' significa: {explanation}"
        else:
            return f"Lo siento, no tengo una explicación para el modismo '{idiom}'."
