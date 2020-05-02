
from flask_wtf import FlaskForm
from wtforms import  TextAreaField
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    description= TextAreaField("Description", validators=[DataRequired()])
    Photo= FileField(validators=[FileRequired(),FileAllowed(['jpg','png'], 'Images Only')])