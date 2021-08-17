import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    '''
    Test class for the user password
    '''
    def setUp(self):
        self.new_user = User(password = 'saucejuice')
    '''
    Setup method that creates an instance of the user class and pass in the password property
    '''

    def test_password_setter(self):
        self.assertTrue(self.new_user.passcode is None)
    '''
    Test case to assertain the the password is being hashed and the passcode contains a value
    '''

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    '''
    Test case to confirm that the application raises an Attribute error on accessing password property
    '''

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('saucejuice'))    
    '''
    Test that confirms that the password_hash can be verified on passing correct password
    '''