from flask import Flask
from flask_migrate import Migrate


from todo.views import main_blueprint
from todo.models import db, Task
from todo.schemas import ma

app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
Migrate(app, db)
ma.init_app(app)

tasks = [Task(title='Angular app_1',
              description='Create application which allow user to store in localstorage cars.'),
         Task(title='RxJs',
              description='Create a script which will make avg of age persons which living in Poland from data.'),
         Task(title='Angular app_2',
              description='Create app to display list of pokemons and details view for each of them.'),
         Task(title='Flask app',
              description='REST API for To-Do list, which allow user to create task, list, update and delete them.'),
         Task(title='Django app',
              description='Blog app with registration and possibility to create new entries and update by authors.'),
         Task(title='Python',
              description='Make solution of three task.')]

with app.app_context():
    db.create_all()
    for task in tasks:
        db.session.add(task)
    db.session.commit()


if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        with app.app_context():
            db.drop_all()
