from functools import wraps
from flask import request, jsonify
import jwt
from auth.keycloak import keycloak

# Secret key for encoding and decoding JWT tokens
SECRET_KEY = 'your_secret_key_here'

def create_token(user_id):
    """Create JWT token."""
    token = jwt.encode({'user_id': user_id}, SECRET_KEY, algorithm='HS256')
    return token

def decode_token(token):
    """Decode JWT token."""
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def require_token(f):
    """Decorator function to require JWT token."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing.'}), 401
        try:
            decoded_token = decode_token(token)
            if 'user_id' in decoded_token:
                return f(*args, **kwargs)
            else:
                return jsonify({'message': 'Invalid token.'}), 401
        except Exception as e:
            return jsonify({'message': str(e)}), 401
    return decorated
