from flask import Flask, jsonify, abort, request, make_response, url_for
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import event, exc, select

app = Flask(__name__, static_url_path = "")

mysql_db_url="mysql://maxlai:pycontw2018@127.0.0.1/demodb"
engine = create_engine(mysql_db_url, echo=True, pool_recycle=3600)
Base = declarative_base()
Base.metadata.reflect(engine)
db_session = scoped_session(sessionmaker(bind=engine))

class Todo_Tasks(Base):
    __table__ = Base.metadata.tables['todo_tasks']


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

def make_public_task(task):
    new_task = {
        "id" : task.id,
        "title" : task.title,
        "description" : task.description,
        "uri" : url_for('get_task', task_id=task.id, _external=True)
    }
    return new_task

@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    # all_tasks = [make_public_task(x) for x in tasks]
    all_tasks = db_session.query(Todo_Tasks).all()
    return jsonify( { 'tasks': [make_public_task(task) for task in all_tasks] } )

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = db_session.query(Todo_Tasks).filter(Todo_Tasks.id == task_id).all()
    if len(task) == 0:
        abort(404)
    return jsonify( { 'task': make_public_task(task[0]) } )

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@event.listens_for(engine, "engine_connect")
def ping_connection(connection, branch):
    if branch:
        # "branch" refers to a sub-connection of a connection,
        # we don't want to bother pinging on these.
        return

    # turn off "close with result".  This flag is only used with
    # "connectionless" execution, otherwise will be False in any case
    save_should_close_with_result = connection.should_close_with_result
    connection.should_close_with_result = False

    try:
        # run a SELECT 1.   use a core select() so that
        # the SELECT of a scalar value without a table is
        # appropriately formatted for the backend
        connection.scalar(select([1]))
    except exc.DBAPIError as err:
        # catch SQLAlchemy's DBAPIError, which is a wrapper
        # for the DBAPI's exception.  It includes a .connection_invalidated
        # attribute which specifies if this connection is a "disconnect"
        # condition, which is based on inspection of the original exception
        # by the dialect in use.
        if err.connection_invalidated:
            # run the same SELECT again - the connection will re-validate
            # itself and establish a new connection.  The disconnect detection
            # here also causes the whole connection pool to be invalidated
            # so that all stale connections are discarded.
            connection.scalar(select([1]))
        else:
            raise
    finally:
        # restore "close with result"
        connection.should_close_with_result = save_should_close_with_result

if __name__ == '__main__':
    app.run(debug = True)
