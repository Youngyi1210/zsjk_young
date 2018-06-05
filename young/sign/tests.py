from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from datetime import datetime
from django.test import Client
from django.contrib.auth.models import User




class IndexPageTest(TestCase):
    '''测试index登录首页'''

    def test_index_page_renders_index_template(self):
        ''' 断言是否用给定的index.html模版响应'''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class LoginActionTest(TestCase):
    ''' 测试登录动作'''

    def setUp(self):
        User.objects.create_user('young123', 'young@mail.com', 'djangoyoung')

    def test_add_author_email(self):
        ''' 测试添加用户 '''
        user = User.objects.get(username="young123")
        self.assertEqual(user.username, "young123")
        self.assertEqual(user.email, "young@mail.com")

    def test_login_action_username_password_null(self):
        ''' 用户名密码为空 '''
        response = self.client.post('/login_action/', {'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password error!", response.content) 

    def test_login_action_username_password_error(self):
        ''' 用户名密码错误 '''
        response = self.client.post('/login_action/', {'username': 'abc', 'password': '123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password error!", response.content)

    def test_login_action_success(self):
        ''' 登录成功 '''
        response = self.client.post('/login_action/', data={'username': 'young123', 'password': 'djangoyoung'})
        self.assertEqual(response.status_code, 302)



