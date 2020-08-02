# author--Li pole
from flask import Flask
from flask import request
from flask import render_template
import utils





app = Flask(__name__)


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/download')
def get_file():
    f = utils.download_file()
    pass


@app.route('/upload')
def upload_file():
    file_path = "F:/picture/"
    file_path = file_path + readfrom
    with open(file_path, 'w') as f:
        f.write(file_source)
    utils.upload_file(file_path)
    pass