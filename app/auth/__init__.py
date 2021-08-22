from flask import Blueprint


# creating a Blueprint instance
auth =  Blueprint('auth', __name__)

from . import views, forms