from flask import Blueprint, render_template
from ..models.users import User

main_bp = Blueprint('main',__name__)

@main_bp.route('/')
def index():
    user_count = User.count_users()
    follows_average = User.average_followers()
    return render_template('index.html', user_count=user_count, follows_average=follows_average)