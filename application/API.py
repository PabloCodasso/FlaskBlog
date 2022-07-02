from flask_restful import Resource
from flask import request
from application.models import User
from application import db


class UsersView(Resource):

    def get(self):
        all_users = User.query.all()
        return {'Users': list(usr.returnJS for usr in all_users)}

    def post(self):
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return {'Message': 'Username already exist!'}
        if User.query.filter_by(email=data['email']).first():
            return {'Message': 'Email already used!'}
        new_user = User(username=data['username'], email=data['email'], about_me=data['about_me'])
        db.session.add(new_user)
        db.session.commit()
        return new_user.returnJS(), 201


class UserView(Resource):

    def get(self, name):
        usr = User.query.filter_by(username=name).first()
        if usr:
            return usr.returnJS()
        return {'Message': 'User not found'}, 404

    def put(self, name):
        data = request.get_json()
        usr = User.query.filter_by(username=name).first()
        if usr:
            usr.username = data['username']
            usr.email = data['email']
        else:
            usr = User(username=name, **data)

        db.session.add(usr)
        db.session.commit()

        return usr.returnJS()

    def delete(self, name):
        usr = User.query.filter_by(username=name).first()
        if usr:
            db.session.delete(usr)
            db.session.commit()
            return {'message': 'Deleted'}
        else:
            return {'message': 'usr not found'}, 404
