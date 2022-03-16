from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('app/index.html')

#
#
# if __name__ == '__main__':
#     main.run(debug=True)
