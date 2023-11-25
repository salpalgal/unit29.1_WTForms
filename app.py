from flask import Flask, render_template, request, redirect
from models import Pet, db, connect_db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route("/")
def show_home():
    """Homepage listing all pets from database."""
    pets = Pet.query.all()

    return render_template("homepage.html" , pets= pets)

@app.route("/add", methods = ["GET", "POST"])
def add_pet():
    """Duo method to show add pet form and handling data from form."""
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name = name, species = species, photo_url = photo_url , age = age, notes = notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_form.html", form = form)

@app.route("/<int:pet_id>", methods = ["GET","POST" ])
def show_pet_details_and_form(pet_id):
    """Duo method to show pet details of pet id along with edit form and handling data from form."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj = pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("pet_details.html", form = form ,pet = pet)