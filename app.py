from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:2795@localhost/authentication"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}


with app.app_context():
    db.create_all()
    
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": 'User not found'}, 404
        return user.to_dict(), 200
    
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"message": 'User not found'}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200
    
    
class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users], 200
    
    def post(self):
        data = request.json
        new_user = User(name=data["name"])
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201

api.add_resource(UserListResource, "/users")
api.add_resource(UserResource, "/users/<int:user_id>")



if __name__ == "__main__":
    app.run(debug=False)