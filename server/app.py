# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>')
def earthquake_by_id(id):
    inst=Earthquake.query.filter_by(id=id).first()
    if inst==None:
        body={
            "message": "Earthquake 9999 not found."
        }
        status=404
    else:
        body=inst.to_dict()
        status=200
    return make_response(body,status)        

@app.route('/earthquakes/magnitude/<float:magnitude>')
def quake_by_mag(magnitude):
    inst = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    if not inst:
        body = {"count": 0, "quakes": []}
        status = 200
    else:
        quake_list = [quake.to_dict() for quake in inst]
        body = {"count": len(inst), "quakes": quake_list}
        status = 200
    return make_response(body, status)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
