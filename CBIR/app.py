# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from search_app import SearchApp
from flask import send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_PHOTOS_DEST'] = 'C:/Users/zhang/Desktop/CBIR/query'
app.config['UPLOAD_FOLDER'] = 'C:/Users/zhang/Desktop/CBIR/result/'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


class UploadForm(FlaskForm):
    photo = FileField(validators=[
        FileAllowed(photos, u'只能上传图片！'), 
        FileRequired(u'文件未选择！')])
    submit = SubmitField(u'上传')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        search = SearchApp(str('./query/' + filename), filename)
        file = search.searchimg()
        file_url_1 = file_url = photos.url(filename)
        file_url_2 = url_for('uploaded_file', filename=filename)
    else:
        file_url_1 = None
        file_url_2 = None
    return render_template('/moban/index.html', form=form, file_url_1=file_url_1, file_url_2=file_url_2)

@app.route('/result/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run()