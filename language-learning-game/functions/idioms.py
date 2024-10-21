# functions/idioms.py

class Idiom:
    def __init__(self, phrase, meaning):
        self.phrase = phrase
        self.meaning = meaning

    def get_details(self):
        return f"Idiom: {self.phrase}, Meaning: {self.meaning}"

class IdiomManager:
    def __init__(self):
        self.idioms = []

    def add_idiom(self, idiom):
        self.idioms.append(idiom)

    def list_idioms(self):
        return [idiom.get_details() for idiom in self.idioms]

# Nueva función para obtener la explicación de un idiom
def get_idiom_explanation(phrase):
    idiom_manager = IdiomManager()
    
    # Puedes añadir algunos idioms aquí para el juego
    idiom_manager.add_idiom(Idiom("break the ice", "To initiate conversation in a social setting."))
    idiom_manager.add_idiom(Idiom("hit the nail on the head", "To be exactly correct about something."))
    idiom_manager.add_idiom(Idiom("spill the beans", "To reveal a secret."))

    for idiom in idiom_manager.idioms:
        if idiom.phrase == phrase:
            return idiom.get_details()
    
    return "Idiom not found."
