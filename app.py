#!/usr/bin/env python3

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_restful import Resource, Api, reqparse

from slack_invite import invite_email

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["50 per hour"]
)

api = Api(app)


class SlackInvite(Resource):

    decorators = [limiter.limit("4/minute")]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, help="please provide an email to sign up", required=True)

    def post(self):
        args = self.parser.parse_args()
        response = invite_email(args.get('email'))
        if response.get('ok'):
            return response, 201
        return response, 400


api.add_resource(SlackInvite, '/slack/invite')

if __name__ == '__main__':
    app.run(debug=True)
