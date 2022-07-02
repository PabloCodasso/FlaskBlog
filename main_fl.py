from application import app, db
from application.models import User, Post


@app.shell_context_processor  # Функция и декоратор для определения контекста консольной оболочки Flask,
def make_shell_context():     # вызываемой командой "flask shell" в сеансе виртуальной среды.
    return {'db': db, 'User': User, 'Post': Post}
