from flask import Blueprint , render_template



agenda = Blueprint('agenda', __name__)

@agenda.route('/Agenda')

def home():
    return render_template("agenda.html")