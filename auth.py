from os import getenv

from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash


auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    """Callback to verify a given password vs the stored one.
    
    Parameters
    ----------
    username : str
        the username
    password : str
        the plaintext password for the user
    """

    if username==getenv('ADMIN_USERNAME') and check_password_hash(getenv('ADMIN_PASSWORD_HASH'), password):
        return username
