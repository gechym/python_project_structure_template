from ..models.todo import TodoBaseModel


def get_todos() -> TodoBaseModel:
    todo = TodoBaseModel()
    todo.id = 1
    todo.content = "alo"
    
    return todo
