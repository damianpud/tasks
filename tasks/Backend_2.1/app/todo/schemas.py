from flask_marshmallow import Marshmallow

ma = Marshmallow()


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'created')


task_schema = TaskSchema(many=True)
