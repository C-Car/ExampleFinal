from flask import Flask, flash, redirect, url_for, render_template, session
from flask import request, jsonify

from flask_sqlalchemy import SQLAlchemy

DB_HOST = "localhost"
DB_NAME = "sandwichmaker"
DB_USERNAME = "root"
DB_Password = "Piedmontred28216!"

database_file = f"mysql+pymysql://{DB_USERNAME}:{DB_Password}@{DB_HOST}:3306/{DB_NAME}"

app = Flask(__name__)
app.secret_key = "mysecret"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


# define a dictionary containing the initial amounts for each resource
initial_amounts = {'ham': 14, 'bread': 18, 'cheese': 24}

# define the reset_resources() function
def reset_resources():
    # update the amount of each resource in the database with its initial value
    for item, amount in initial_amounts.items():
        resource = Resource.query.filter_by(item=item).first()
        resource.amount = amount
        db.session.commit()


class Resource(db.Model):
    __tablename__ = 'resources'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/resource")
def resource():
    resources = Resource.query.all()
    resources_dict = [{"amount": r.amount, "item": r.item} for r in resources]
    return jsonify(resources_dict)

@app.route("/makesmall", methods=["POST"])
def makesmall():
    # get the sandwich resources from the database
    resources = Resource.query.all()
    # set the required resources for a small sandwich
    required_resources = {"bread": 1, "ham": 1, "cheese": 2}
    # double the required resources for a medium sandwich
    for key in required_resources:
        required_resources[key] *= 1
    # check if there are enough resources to make the sandwich
    for resource in resources:
        if resource.item in required_resources and resource.amount < required_resources[resource.item]:
            # if there are not enough resources, return an error message
            return jsonify({"message": "Error: not enough resources to make a medium sandwich"})
    # if there are enough resources, update the database and return a success message
    for resource in resources:
        if resource.item in required_resources:
            resource.amount -= required_resources[resource.item]
            db.session.commit()
    return jsonify({"message": "Medium sandwich successfully made"})

@app.route("/makemedium", methods=["POST"])
def makemedium():
    # get the sandwich resources from the database
    resources = Resource.query.all()
    # set the required resources for a small sandwich
    required_resources = {"bread": 1, "ham": 1, "cheese": 2}
    # double the required resources for a medium sandwich
    for key in required_resources:
        required_resources[key] *= 2
    # check if there are enough resources to make the sandwich
    for resource in resources:
        if resource.item in required_resources and resource.amount < required_resources[resource.item]:
            # if there are not enough resources, return an error message
            return jsonify({"message": "Error: not enough resources to make a medium sandwich"})
    # if there are enough resources, update the database and return a success message
    for resource in resources:
        if resource.item in required_resources:
            resource.amount -= required_resources[resource.item]
            db.session.commit()
    return jsonify({"message": "Medium sandwich successfully made"})

@app.route("/makelarge", methods=["POST"])
def makelarge():
    # get the sandwich resources from the database
    resources = Resource.query.all()
    # set the required resources for a small sandwich
    required_resources = {"bread": 1, "ham": 1, "cheese": 2}
    # double the required resources for a medium sandwich
    for key in required_resources:
        required_resources[key] *= 4
    # check if there are enough resources to make the sandwich
    for resource in resources:
        if resource.item in required_resources and resource.amount < required_resources[resource.item]:
            # if there are not enough resources, return an error message
            return jsonify({"message": "Error: not enough resources to make a large sandwich"})
    # if there are enough resources, update the database and return a success message
    for resource in resources:
        if resource.item in required_resources:
            resource.amount -= required_resources[resource.item]
            db.session.commit()
    return jsonify({"message": "Large sandwich successfully made"})

@app.route("/reset", methods=["POST"])
def reset():
    resources = Resource.query.all()
    for resource in resources:
        if resource.item == "ham":
            resource.amount = 18
        elif resource.item == "bread":
            resource.amount = 14
        elif resource.item == "cheese":
            resource.amount = 24
    db.session.commit()

    # return a success message
    return jsonify({"message": "Resources reset"})


@app.route('/addresource', methods=['GET', 'POST'])
def add_resource():
    if request.method == 'POST':
        if not request.form['item'] or not request.form['amount']:
            flash('Please enter all the fields', 'error')
        else:
            resource = Resource(request.form['item'], request.form['amount'])

            db.session.add(resource)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('resource'))
    return render_template('resources/add.html')


@app.route('/updateresource/<int:id>/', methods=['GET', 'POST'])
def update_resource(id):
    if request.method == 'POST':
        if not request.form['item'] or not request.form['amount']:
            flash('Please enter all the fields', 'error')
        else:
            resource = Resource.query.filter_by(id=id).first()
            resource.item = request.form['item']
            resource.amount = request.form['amount']
            db.session.commit()

            flash('Record was successfully updated')
            return redirect(url_for('resource'))
    data = Resource.query.filter_by(id=id).first()
    return render_template("resources/update.html", data=data)


@app.route('/deleteresource/<int:id>/', methods=['GET', 'POST'])
def delete_resource(id):
    if request.method == 'POST':
        resource = Resource.query.filter_by(id=id).first()
        db.session.delete(resource)
        db.session.commit()

        flash('Record was successfully deleted')
        return redirect(url_for('resource'))
    data = Resource.query.filter_by(id=id).first()
    return render_template("resources/delete.html", data=data)

class Sandwich(db.Model):
    __tablename__ = 'sandwiches'
    id = db.Column(db.Integer, primary_key=True)
    sandwich_size = (db.Column(db.String(50), nullable=False))
    price = db.Column(db.DECIMAL(5, 2), nullable=False)
    
    def __init__(self, sandwich_size, price):
        self.sandwich_size = sandwich_size
        self.price = price

@app.route("/sandwich")
def sandwich():
    return render_template("sandwiches/list.html", sandwich=Sandwich.query.all())
   
if __name__ == '__main__':
    app.run(port=3001, host="localhost", debug=True)

