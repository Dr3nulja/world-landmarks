from app import create_app, db
from sqlalchemy import text

app = create_app()

with app.app_context():
    try:
        db.session.execute(text('SELECT 1'))
        print("Успешное подключение к базе")
    except Exception as e:
        print("Не получилось подключиться к базе", e)

if __name__ == '__main__':
    app.run(debug=True)
