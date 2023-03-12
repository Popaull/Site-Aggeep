from flask import Flask

def create_app():
    app=Flask(__name__)
    app.static_folder = 'static'
    app.config['SECRET_KEY']='sdf'
    from .views import views
    from .info import  info
    from .philo import contactez
    from .guide  import guide
    from .agenda import agenda
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(contactez, url_prefix='/')
    app.register_blueprint(info, url_prefix='/')
    app.register_blueprint(guide, url_prefix='/')
    app.register_blueprint(agenda, url_prefix='/')

    
    return app