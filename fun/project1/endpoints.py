from flask import Blueprint
from flask import render_template


proj1_app = Blueprint('project1_handlers', __name__)


@proj1_app.route('/')
def main():
    return render_template('index.html')
