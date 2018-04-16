from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[InputRequired(message='Description is required')])
    upload = FileField('Image', validators=[FileRequired('Please input a file'), FileAllowed(['jpg', 'png'], 'Images only!')])
