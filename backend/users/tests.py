from urllib import response
from urllib.parse import urlparse

from django.test import TestCase, Client

from django.urls import reverse
from django.contrib.auth import get_user_model


from .serializers import CustomUserSerializer

from pprint import pp


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)


class UsersViewsTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        self.User = get_user_model()
        self.email = 'iftakhar@gmail.com'
        self.password = 'iekd*ldk3lLkd9'
        self.user: self.User = self.User.objects.create_user(
            email=self.email,
            password=self.password,
            first_name='iftakhar',
            last_name='husan'
            )

    def tearDown(self) -> None:
        self.user.delete()


    def login_user(self, email=None, password=None):
        if email == None and password == None:
            email, password = self.email, self.password
        return self.client.post(path=reverse('users:login'), data={'username': email, 'password': password})


    # user_login view tests
    def test_user_login_with_empty_credentials(self):
        response = self.login_user('', '')
        self.assertEqual(response.status_code, 400)

        data = response.json()
        expected_data = {
            'success': False,
            'errors': {
                'username': ['This field is required!'],
                'password': ['This field is required!']
            }
        }
        self.assertDictEqual(data, expected_data)

    def test_user_login_with_incorrect_credentials(self):
        invalid_credentials = [
            (self.email, 'invalid_password'),
            ('invalidemailaddress@gmail.com', self.password),
            ('invalidemailaddress@gmail.com', 'invalid_password')
        ]
        for email, password in invalid_credentials:
            response = self.login_user(email, password)

            data = response.json()
            expected_data = {'success': False,
                             'errors': {'password': ['Invalid credentials!']}
                            }

            self.assertEqual(response.status_code, 400)
            self.assertDictEqual(data, expected_data)

    def test_user_login_with_correct_credentials_and_disallowed_http_method(self):
        response = self.client.put(path=reverse('users:login'), data={
                                   'username': self.email, 'password': self.password})
        self.assertEqual(response.status_code, 405)

    def test_user_login_with_correct_credentials(self):
        response = self.login_user()
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, 200)

        data = response.json()
        expected_data = {'success': True,
                         'data': CustomUserSerializer(self.user).data}
        self.assertDictEqual(data, expected_data)


    # user_logout view tests
    def test_user_logout_when_already_logged_out(self):
        self.client.logout()
        response = self.client.get(path=reverse('users:logout'))

        self.assertGreaterEqual(response.status_code, 300)
        self.assertLessEqual(response.status_code, 399)
        self.assertEqual(urlparse(response.url).path, reverse('users:login'))

    def test_user_logout_with_disallowed_http_method(self):
        response = self.client.post(path=reverse('users:logout'))
        self.assertGreaterEqual(response.status_code, 405)

    def test_user_logout_when_logged_in(self):
        self.client.force_login(self.user)
        response = self.client.get(path=reverse('users:logout'))
        self.assertGreaterEqual(response.status_code, 200)

        data = response.json()
        expected_data = {'success': True}
        self.assertDictEqual(data, expected_data)

        # try to fetch user_details
        response = self.client.get(path=reverse('users:details'))
        
        self.assertGreaterEqual(response.status_code, 300)
        self.assertLessEqual(response.status_code, 399)
        self.assertEqual(urlparse(response.url).path, reverse('users:login'))


    # user_details view tests
    def test_user_details_with_disallowed_method(self):
        response = self.client.post(reverse('users:details'))
        self.assertEqual(response.status_code, 405)

    def test_user_details_without_authorization(self):
        self.client.logout()

        response = self.client.get(reverse('users:details'))

        self.assertGreaterEqual(response.status_code, 300)
        self.assertLessEqual(response.status_code, 399)
        self.assertEqual(urlparse(response.url).path, reverse('users:login'))

    def test_user_details_with_incorrect_http_method(self):
        response = self.client.post(reverse('users:details'))
        self.assertEqual(response.status_code, 405)

    def test_user_details_with_authorization_and_correct_http_method(self):
        self.client.force_login(self.user)
        self.user.refresh_from_db()

        response = self.client.get(reverse('users:details'))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        expected_data = {
            'success': True,
            'data': CustomUserSerializer(self.user).data
        }
        self.assertDictEqual(data, expected_data)


    # user_change_password view tests
    def test_user_change_password_with_disallowed_http_methods_and_unauthorized(self):
        self.client.logout()
        response = self.client.get(reverse('users:change_password'))
        self.assertEqual(response.status_code, 405)

    def test_user_change_password_with_disallowed_http_methods_and_authorized(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('users:change_password'))
        self.assertEqual(response.status_code, 405)
    
    def test_user_change_password_without_authorization(self):
        self.client.logout()
        response = self.client.post(reverse('users:change_password'))

        self.assertGreaterEqual(response.status_code, 300)
        self.assertLessEqual(response.status_code, 399)
        self.assertEqual(urlparse(response.url).path, reverse('users:login'))
    
    def test_user_change_password_without_any_data(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('users:change_password'))
        self.assertEqual(response.status_code, 400)
   
    def test_user_change_password_with_different_password(self):
        self.client.force_login(self.user)
        different_passwords = [
            ('password1', ''),
            ('password1', 'password2'),
            ('superStrongp44sword', 'superStrongp44$word'),
        ]
        for password1, password2 in different_passwords:
            response = self.client.post(
                path=reverse('users:change_password'),
                data={'password1': password1, 'password2': password2})
            self.assertEqual(response.status_code, 400)

            data = response.json()
            expected_structure = {'success': False, 'help': {}, 'errors': {}}
            self.assertEqual(data.get('success', None), expected_structure.get('success'))
            self.assertTrue(set(expected_structure.keys()).issubset(set(data.keys())))
    
    def test_user_change_password_with_weak_passwords(self):
        self.client.force_login(self.user)
        weak_passwords = [
            'password',
            '12345678',
            'qwertyui',
            self.email,
            'iftakhar',
            'iftakharhusan',
            'husaniftakhar',
            'husanqwe'
        ]
        for weak_password in weak_passwords:
            response = self.client.post(
                path=reverse('users:change_password'),
                data={'password1': weak_password, 'password2': weak_password})
            self.assertEqual(response.status_code, 400)

            data = response.json()
            expected_structure = {'success': False, 'help': {}, 'errors': {}}

            self.assertEqual(data.get('success', None), expected_structure.get('success', None))
            # assert data dictionary contains all keys present in expected_structure dictionary
            self.assertTrue(set(expected_structure.keys()).issubset(set(data.keys())))

    def test_user_change_password_with_strong_password(self):
        strong_passwords = [
            'superStrongP44$$Word',
            'salkdfjdlKkldl389--38sdf',
            'lksdjLKdkdl293#lsdk',
            'kdieknckeoeufeiwowo'
        ]
        for strong_password in strong_passwords:
            self.client.force_login(self.user)
            response = self.client.post(
                path=reverse('users:change_password'),
                data={'password1': strong_password, 'password2': strong_password})
            self.assertEqual(response.status_code, 200)

            data = response.json()
            expected_data = {'success': True}
            self.assertDictEqual(data, expected_data)
