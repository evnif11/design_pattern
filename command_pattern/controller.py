from dataclasses import dataclass, field
from transaction import Transaction

@dataclass
class TextEditorController:
    undo_stack: list[Transaction] = field(default_factory=list)
    redo_stack: list[Transaction] = field(default_factory=list)

    def execute(self, transaction: Transaction) -> None:
        transaction.execute()
        self.redo_stack.clear()
        self.undo_stack.append(transaction)
    
    def undo(self) -> None:
        if self.undo_stack:
            transaction = self.undo_stack.pop()
            transaction.undo()
            self.redo_stack.append(transaction)

    def redo(self) -> None:
        if self.redo_stack:
            transaction = self.redo_stack.pop()
            transaction.redo()
            self.undo_stack.append(transaction)