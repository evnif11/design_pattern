from dataclasses import dataclass

@dataclass
class TextEditor:
    text: str = ""

    def insert(self, text: str) -> None:
        self.text += text

    def delete(self, num_chars: int) -> None:
        self.text = self.text[:-num_chars]

    def undo(self) -> None:
        pass

    def redo(self) -> None:
        pass

    def print_text(self) -> None:
        print(self.text)