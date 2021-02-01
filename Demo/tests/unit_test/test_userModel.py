import unittest
from unittest import mock
from models.user import UserModel


class TestUserModel(unittest.TestCase):
    expect_get_user_ok = {
        'message': '',
        'name': 'Jef',
        'password': 'jef123'
    }

    expect_get_user_fail = {
        'message': 'username not exist!'
    }

    expect_add_user_ok = {
        'message': 'Insert user success',
        'user': 'Jef'
    }

    expect_add_user_fail = {
        'message': 'User already exist!'
    }

    expect_get_user_list = [
        {'name': 'Jef', 'password': 'jef123'},
        {'name': 'Zoey', 'password': 'zoey123'}
    ]

    expect_get_empty_user_list = []

    expect_verify_user_account_ok = {
        'message': 'success',
        'name': 'Jef',
        'password': 'jef123'
    }

    expect_verify_user_account_fail = {
        'message': 'User Not found'
    }

    mock_user = UserModel('fake_name', 'fake_pwd')
    def test_get_user_return_user(self):
        with mock.patch('models.user.UserModel.get_user') as model_mock:
            model_mock.return_value = {
                'message': '',
                'name': 'Jef',
                'password': 'jef123'
            }
            fake_user = self.mock_user.get_user('fake_name')
            model_mock.assert_called_once()
            self.assertEqual(self.expect_get_user_ok, fake_user)
    
    def test_get_user_return_username_not_exist(self):
        with mock.patch('models.user.UserModel.get_user') as model_mock:
            model_mock.return_value = {
                'message': 'username not exist!',
            }
            fake_user = self.mock_user.get_user('fake_name')
            model_mock.assert_called_once()
            self.assertEqual(self.expect_get_user_fail, fake_user)
            
    def test_add_user_return_insert_user_success(self):
        with mock.patch('models.user.UserModel.add_user') as model_mock:
            model_mock.return_value = {
                'message': 'Insert user success',
                'user': 'Jef'
            }
            fake_user = self.mock_user.add_user()
            model_mock.assert_called_once()
            self.assertEqual(self.expect_add_user_ok, fake_user)
    
    def test_add_user_return_user_already_exist(self):
        with mock.patch('models.user.UserModel.add_user') as model_mock:
            model_mock.return_value = {
                'message': 'User already exist!'
            }
            fake_user = self.mock_user.add_user()
            model_mock.assert_called_once()
            self.assertEqual(self.expect_add_user_fail, fake_user)
    
    def test_get_all_user_return_users(self):
        with mock.patch('models.user.UserModel.get_all_user') as model_mock:
            model_mock.return_value = [
                {'name': 'Jef', 'password': 'jef123'},
                {'name': 'Zoey', 'password': 'zoey123'}
            ]
            fake_user_list = self.mock_user.get_all_user()
            model_mock.assert_called_once()
            self.assertEqual(self.expect_get_user_list, fake_user_list)
    
    def test_get_all_user_return_empty_user_list(self):
        with mock.patch('models.user.UserModel.get_all_user') as model_mock:
            model_mock.return_value = []
            fake_user_list = self.mock_user.get_all_user()
            model_mock.assert_called_once()
            self.assertEqual(self.expect_get_empty_user_list, fake_user_list)
    
    def test_verify_user_account_return_success(self):
        with mock.patch('models.user.UserModel.verify_user_account') as model_mock:
            model_mock.return_value = {
                'message': 'success',
                'name': 'Jef',
                'password': 'jef123'
            }
            fake_verify_success = self.mock_user.verify_user_account('fake_name', 'fake_pwd')
            model_mock.assert_called_once()
            self.assertEqual(self.expect_verify_user_account_ok, fake_verify_success)
    
    def test_verify_user_account_return_user_not_found(self):
        with mock.patch('models.user.UserModel.verify_user_account') as model_mock:
            model_mock.return_value = {
                'message': 'User Not found'
            }
            fake_verify_fail = self.mock_user.verify_user_account('fake_name', 'fake_pwd')
            model_mock.assert_called_once()
            self.assertEqual(self.expect_verify_user_account_fail, fake_verify_fail)