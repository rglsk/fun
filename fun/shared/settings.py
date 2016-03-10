import os


DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_SERVICE = os.environ['DB_SERVICE']
DB_PORT = os.environ['DB_PORT']
SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME)


INTERESTING_ROBOT_PHRASES = ['pilne', 'private', 'prywatne', 'hasla',
                             'zakazane', 'passwords', 'naked', 'nagie', 'nago',
                             'notpublic', 'forbidden', 'zabronione', 'dupa',
                             'raport', 'report']

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = int(os.environ.get('DEBUG', '0'))
