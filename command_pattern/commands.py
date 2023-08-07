from dataclasses import dataclass
from text_editor import TextEditor

@dataclass
class Insert:
    text_editor: TextEditor
    text: str

    def execute(self) -> None:
        self.text_editor.insert(self.text)

    def undo(self) -> None:
        self.text_editor.delete(len(self.text))

    def redo(self) -> None:
        self.execute()

@dataclass
class Delete:
    text_editor: TextEditor
    num_chars: int

    def execute(self) -> None:
        self.text_editor.delete(self.num_chars)

    def undo(self) -> None:
        pass

    def redo(self) -> None:
        pass
