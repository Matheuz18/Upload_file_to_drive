from flask import Flask, render_template
from flask_cors import CORS
from flask import request
from cortex.upload_drive import file_upload
import os

app = Flask(__name__)
CORS(app)


@app.route("/upload/file", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        data = request.json

        # Get the folder id from the given link
        if "/" in data["drive_path"]:
            drive_link = data["drive_path"].split('/')
        else:
            drive_link = data["drive_path"]

        folder_name = drive_link[len(drive_link) - 1]

        # Upload the build to given drive folder
        resp = file_upload(folder_name, data["file_name"])

        return resp


if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
