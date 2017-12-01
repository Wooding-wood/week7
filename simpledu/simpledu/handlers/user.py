from flask import Blueprint, render_template
from simpledu.models import User, Course
#from flask_sqlalchemy import SQLAlchemy

user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<userid>')
def print_user(userid):
    user = {'id':'', 'name':'', 'course': []}
    getuser = User.query.filter_by(username=userid).first()
    if getuser is not None:
        user['id'] = getuser.id
        user['name'] = getuser.username
        for course in getuser.publish_courses:
            user['course'].append(course.name)

        return render_template('user.html', user = user)
    else:
        return render_template('404.html')
