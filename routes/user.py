from flask import Blueprint, render_template

user_route = Blueprint('user', __name__)

@user_route.route('/user/<user_name>', methods=['POST', 'GET'])
def user(user_name):
    return render_template('user.html', user_name=user_name)
