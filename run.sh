export FLASK_APP=project
export FLASK_DEBUG=1

flask db init
flask db migrate
flask db upgrade

flask run
