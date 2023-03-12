from flask import Blueprint , render_template



guide = Blueprint('guide', __name__)

@guide.route('/Quisommes-nous')

def home():
    return render_template("guide.html")