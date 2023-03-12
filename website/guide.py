from flask import Blueprint , render_template



guide = Blueprint('guide', __name__)

@guide.route('/Guide_de_la_vie_étudiante')

def home():
    return render_template("guide.html")