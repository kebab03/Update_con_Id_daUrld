from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db= SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    #rating = db.Column(db.Integer, nullable=False, default=0)
    description=db.Column(db.String(120))
    def __repr__(self):
        return f"{self.name} is rated {self.description}"

@app.route('/')
def index():
    return 'testimonial.html'




@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    output =[]
    for drink in drinks:
        drink_data= {'name': drink.name,'description': drink.description}

        output.append(drink_data)
        print(output)

    return {"drinks": output}


@app.route('/drinks/<id>')
def get_drink(id):
    drink=Drink.query.get(id)
    return {"name": drink.name,'description':drink.description}


@app.route('/drinks/<md>', methods=['POST'])
def add_drink(md):
    drink = Drink(id=md, name=request.json['name'],description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    #drink = Drink.query.get(id)
    drink = Drink.query.get(id)
    if drink is None:
        return {"error ": "not found"}
    db.session.delete(drink)
    db.session.commit()
    #drink   REST API Crash Course - Introduction + Full Python API Tutorial
    return {"message": "drink.id"}
if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
    delete_drink(2)


