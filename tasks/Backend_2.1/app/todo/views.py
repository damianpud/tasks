from flask import Blueprint
from .models import Task, db
from .schemas import task_schema
from flask import request, jsonify

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/', methods=['GET'])
def all_tasks():
    tasks = Task.query.all()
    result = task_schema.dump(tasks)
    return jsonify(result)


@main_blueprint.route('/create_task', methods=['POST'])
def create_task():
    title = request.json['title']
    description = request.json['description']
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({
        "id": new_task.id,
        "title": new_task.title,
        "description": new_task.description,
    })


@main_blueprint.route('/get_task/<task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.filter_by(id=task_id)
    result = task_schema.dump(task)
    return jsonify(result)


@main_blueprint.route('/update_task/<task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    title = request.json['title']
    description = request.json['description']
    task.title = title
    task.description = description
    db.session.commit()
    return jsonify({"success": "successfully updated"})


@main_blueprint.route("/delete_task/<task_id>", methods=['DELETE'])
def delete(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"success": "successfully deleted"})


