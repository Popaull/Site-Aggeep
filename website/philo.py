from flask import Blueprint , render_template
from apscheduler.schedulers.background import BackgroundScheduler






contactez = Blueprint('contactez', __name__)

@contactez.route('/contactez_nous')

def home():
    return render_template("contactez.html")
    
 
