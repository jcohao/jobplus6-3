from flask import Blueprint, render_template

jobs = Blueprint('jobs', __name__, url_prefix='/jobs')
