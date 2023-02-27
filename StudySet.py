from Flashcard import * 

class StudySet: 
    def __init__(self) -> None:
        self.set_of_flashcards = set()
    
    def add_flashcard(flashcard : Flashcard) -> None:
        self.set_of_flashcards.add(flashcard)

    def print_set(self) -> None:
        print(self.set_of_flashcards)
    