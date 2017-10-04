import unittest

from app import db, app
from instance.config import app_config


class ApiTestCase(unittest.TestCase):
    
    def setUp(self):        
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    