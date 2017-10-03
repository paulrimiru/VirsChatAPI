import os
import json
import unittest

from app import create_app, db

class UserTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.user = {'username':'mike paul', 'usertype':'support', 'email':'mike@support.com', 'password':'1234567'}
        self.usercredential = {'email':'mike@support.com', 'password':'1234567'}

        with self.app.app_context():
            db.create_all()
    def test_usercreation(self):
        """Test to ensure users are registered successfully"""
        response = self.client().post('/users/', data=self.user)
        self.assertEquals(response.status_code, 201)
    def test_getallusers(self):
        """Test to get all the users"""
        response = self.client().post('/users/', data=self.user)
        self.assertEquals(response.status_code, 201)
        response = self.client().get('/users/')
        self.assertIn('support', str(response.data))
    def test_userlogin(self):
        """test user login"""
        response = self.client().post('/users/', data=self.user)
        self.assertEquals(response.status_code, 201)

        response = self.client().post('/users/', data=self.usercredential)
        self.assertIn('login successful', str(response.data))
        self.assertEquals(response.status_code, 201)
    def test_getuser(self):
        """test get specific user"""
        response = self.client().post('/users/', data=self.user)
        self.assertEquals(response.status_code, 201)

        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/user/{}'.format(result_in_json['email']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('mike@support.com', str(result.data))
        
    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
    
if __name__ == '__main__':
    unittest.main()
    