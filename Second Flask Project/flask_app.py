from flask import Flask
import sys
sys.path.insert(1, "PATH TO LOCAL PYTHON PACKAGES")  #OPTIONAL: Only if need to access Python packages installed on a local (non-global) directory
sys.path.insert(2, "PATH TO FLASK DIRECTORY")      #OPTIONAL: Only if you need to add the directory of your flask app



app = Flask(__name__)

@app.route('/allfruits')
def print_fruits():
    from function import allfruits
@app.route('/Mathoperation')
def calculator():
    from function import Mathoperation

