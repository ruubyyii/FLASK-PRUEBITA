from jwt import encode, decode, exceptions
from os import getenv
from flask import jsonify
from datetime import datetime, timezone, timedelta

def write_token(data:dict):

    token = encode(payload={**date, 'exp':datetime.now(tz=timezone.utc) + timedelta(minutes=1)}, key=getenv=('SECRET_KEY'), algorithm='HS256')

    return token.encode('UTF-8')

def validate_token(token, output=False):

    try:
        if output:
            return decode(token, key=getenv('SECRET'), algorithms=['HS256'])

        decode(token, key=getenv('SECRET'), algorithms=['HS256'])

    except exceptions.DecodeError as e:

        response = jsonify({"message":"Invalid Token"})
        response.status_code = 401

        return response

    except exceptions.ExpiredSignatureError as e:

        response = jsonify({"message":"Token Expired"})
        response.status_code = 401

        return response