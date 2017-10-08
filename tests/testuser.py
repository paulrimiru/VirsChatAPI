import json

from app import db, app
from app.utils.testing import ApiTestCase
from app.users.models import PasswordReset

import unittest
class UserApiTest(ApiTestCase):

    user_data = {
        'username': 'admin something',
        'usertype': 'admin',
        'email': 'something@email.com',
        'password': '123456',
    }

    def test_registration(self):
        response = self.app.post('/api/v1/user', data=self.user_data)
        data = json.loads(response.data)

        assert data['id'] == 1
        assert len(data['token']) > 10

    def test_duplicate_registration(self):
        response = self.app.post('/api/v1/user', data=self.user_data)
        assert response.status_code == 201

        response = self.app.post('/api/v1/user', data=self.user_data)
        assert response.status_code == 409

    def test_get_user(self):
        response = self.app.post('/api/v1/user', data=self.user_data)
        data = json.loads(response.data)
        headers = {'Authorization': data['token']}

        response = self.app.get('/api/v1/user', headers=headers)
        data = json.loads(response.data)
        assert data['email'] == 'something@email.com'

    def test_password_reset(self):
        response = self.app.post('/api/v1/user', data=self.user_data)
        assert response.status_code == 201

        response = self.app.post('/api/v1/password-reset/request', data={
            'email': 'something@email.com'
        })
        assert response.status_code == 201

        pw_reset = db.session.query(PasswordReset).first()

        response = self.app.post('/api/v1/password-reset/confirm', data={
            'code': "bad code",
            'password': 'abc123'
        })
        assert response.status_code == 401

        response = self.app.post('/api/v1/password-reset/confirm', data={
            'code': pw_reset.code,
            'password': 'abc123'
        })
        assert response.status_code == 200

        response = self.app.post('/api/v1/authenticate', data={
            'email': 'something@email.com',
            'password': 'abc123'
        })
        print(response.status_code)
        assert response.status_code == 200
        