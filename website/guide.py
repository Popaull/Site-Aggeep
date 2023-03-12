from flask import Blueprint , render_template



guide = Blueprint('guide', __name__)

@guide.route('/Qui-sommes-nous')

def home():
    return render_template("qui-sommes-nous.html")