import requests
import unittest

class TestAPIRequest(unittest.TestCase):
    basic_url = 'http://127.0.0.1:5000/'

    def test_get_user_return_success(self):
        url = self.basic_url + 'getuser/test_api_user'
        response = requests.get(url)
        response_dict = eval(response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual('test_api_user', response_dict['name'])
        self.assertEqual('test_api_pwd', response_dict['password'])

    def test_get_user_return_user_not_exist(self):
        url = self.basic_url + 'getuser/not_exist_user'
        response = requests.get(url)
        response_dict = eval(response.text)
        self.assertEqual(403, response.status_code)
        self.assertEqual('username not exist!', response_dict['message'])
    
    @unittest.skip("skip first for not influence the db")
    def test_add_user_return_success(self):
        url = self.basic_url + 'adduser/'
        user = {
            'name': 'test_add_user',
            'password': 'test_add_pwd'
        }
        response = requests.post(url, data=user)
        response_dict = eval(response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual('Insert user success', response_dict['message'])

    def test_add_user_return_user_already_exist(self):
        url = self.basic_url + 'adduser/'
        user = {
            'name': 'user_exist',
            'password': 'pwd_exist'
        }
        response = requests.post(url, data=user)
        response_dict = eval(response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual('User already exist!', response_dict['message'])
    
    def test_verify_user_account_return_success(self):
        url = self.basic_url + 'verifyuser/test_api_user/test_api_pwd/'
        response = requests.get(url)
        response_dict = eval(response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual('success', response_dict['message'])
        self.assertEqual('test_api_user', response_dict['name'])
        self.assertEqual('test_api_pwd', response_dict['password'])
    
    def test_verify_user_account_return_user_not_found(self):
        url = self.basic_url + 'verifyuser/not_exist_user/not_exist_pwd/'
        response = requests.get(url)
        response_dict = eval(response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual('User Not found', response_dict['message'])

    def test_get_all_user_return_user_list(self):
        url = self.basic_url + 'allusers/'
        response = requests.get(url)
        response_list = eval(response.text)
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response_list) != 0)

    


    