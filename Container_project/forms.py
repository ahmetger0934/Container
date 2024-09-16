from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    length = FloatField('Length of the product (cm)', validators=[DataRequired()])
    width = FloatField('Width of the product (cm)', validators=[DataRequired()])
    height = FloatField('Height of the product (cm)', validators=[DataRequired()])
    container = SelectField('Choose Container', choices=[
        ('container_1', 'Container 1'),
        ('container_2', 'Container 2'),
        ('container_3', 'Container 3'),
        ('container_4', 'Container 4'),
        ('container_5', 'Container 5'),
        ('container_6', 'Container 6')
    ], validators=[DataRequired()])
    submit = SubmitField('Calculate')