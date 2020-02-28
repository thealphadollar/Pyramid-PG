from datetime import datetime
from pyramid.view import view_config
from todo.models import Task, User

from sqlalchemy import _or

INCOMING_DATE_FMT = '%d/%m/%Y %H:%M:%S'

@view_config(route_name="tasks", request_method="POST", renderer='json')
def create_task(request):
    """Create a task for one user."""
    response = request.response
    response.headers.extend({'Content-Type': 'application/json'})
    user = request.dbsession.query(User).filter_by(username=request.matchdict['username']).first()
    if user:
        due_date = request.json['due_date']
        task = Task(
            name=request.json['name'],
            note=request.json['note'],
            due_date=datetime.strptime(due_date, INCOMING_DATE_FMT) if due_date else None,
            completed=bool(request.json['completed']),
            user_id=user.id
        )
        request.dbsession.add(task)
        response.status_code = 201
        return {'msg': f'task added for {request.matchdict["username"]}'}
    response.status_code = 404
    return {'msg': 'user not found!'}

@view_config(route_name="register", request_method="POST", renderer='json')
def create_user(request):
    """
    Create a new user.
    """
    response = request.response
    response.headers.extend({'Content-Type': 'application/json'})
    user = request.dbsession.query(User).filter(_or(User.username==request.json['username'], User.email==request.json['email'] )).first()
    if user is None:
        user = User(
            username = request.json['username'],
            email = request.json['email'],
            password = request.json['password']
        )
        request.dbsession.add(user)
        response.status_code = 201
        return {'msg': 'user added'}
    response.status_code = 403
    return {'mst': 'username or email already exists'}