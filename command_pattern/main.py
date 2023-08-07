from text_editor import TextEditor
from controller import TextEditorController
from commands import Insert, Delete

def main() -> None:
    # Test the text editor
    editor = TextEditor()
    controller = TextEditorController()
    

    controller.execute(Insert(editor, "Hello"))
    controller.execute(Insert(editor, " World!"))
    editor.print_text()  # Output: Hello World!
    
    controller.undo() 
    editor.print_text() # Output: Hello
    controller.redo() 
    editor.print_text() # Output: Hello World!


    controller.execute(Delete(editor, 6))
    editor.print_text()  # Output: Hello


if __name__ == "__main__":
    main()