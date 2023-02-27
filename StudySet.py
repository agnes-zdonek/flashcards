from Flashcard import * 
import json

class StudySet: 
    def __init__(self) -> None:
        self.set_of_flashcards = set()
    
    def add_flashcard(self, flashcard : Flashcard) -> None:
        self.set_of_flashcards.add(flashcard)

    def print_set(self) -> None:
        print(self.set_of_flashcards)
    
    def read_flashcards(self, file_path : str) -> None:
        with open(file_path, 'r') as file:
            data = json.load(file)
            flashcards = data['flashcards']
            for card in flashcards:
                self.add_flashcard(Flashcard(card['question'], card['answer']))