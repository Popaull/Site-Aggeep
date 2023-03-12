from website import create_app

import os
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, abort, render_template, jsonify,json,url_for



        
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000 ,debug=True)


