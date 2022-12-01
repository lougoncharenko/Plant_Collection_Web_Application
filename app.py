
############################################################
# Import Packages
############################################################

from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

############################################################
# SETUP
############################################################

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/plantsDatabase"
mongo = PyMongo(app)

############################################################
# ROUTES
############################################################

@app.route('/')
def plants_list():
    """Display the plants list page."""

    # TODO: Replace the following line with a database call to retrieve *all*
    # plants from the Mongo database's `plants` collection.
    plants_data = mongo.db.plants_data.find()
    context = {
        'plants': plants_data,
    }
    return render_template('plants_list.html', **context)

@app.route('/about')
def about():
    """Display the about page."""
    return render_template('about.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    """Display the plant creation page & process data from the creation form."""
    if request.method == 'POST':
        name = request.form['plant_name']
        variety = request.form['variety']
        photo = request.form['photo']
        date = request.form['date_planted']
      
        new_plant = {
            'name': name,
            'variety': variety,
            'photo_url': photo,
            'date_planted': date
        }
        id = mongo.db.plants_data.insert_one(new_plant)
        return redirect(url_for('detail', plant_id=id))

    else:
        return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)