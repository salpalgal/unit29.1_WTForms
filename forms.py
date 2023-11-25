from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import Optional, URL, InputRequired, AnyOf, NumberRange

class AddPetForm(FlaskForm):
    
    name = StringField("pet name", validators=[InputRequired()])
    species = StringField(" species of pet", validators=[InputRequired(), AnyOf(values = ['cat', 'dog', 'porcupine'])])
    photo_url = StringField("photo url" , validators=[Optional(),])
    age = IntegerField("pet age", validators= [Optional(), NumberRange(min=0, max= 30)])
    notes = StringField("additional note", validators= [Optional()])

class EditPetForm(FlaskForm):

    photo_url = StringField("photo url",validators=[Optional(),URL()])
    notes = StringField("additional note", validators= [Optional()])
    available = BooleanField("available", validators=[Optional()])
