from flask import Blueprint

course = Blueprint('course', __name__, url_prefix='/courses')

@course.route('/<coursename>')
def course_index(coursename):
    return 'course is:' + coursename
