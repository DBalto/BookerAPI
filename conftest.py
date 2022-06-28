from pytest import fixture

from config import Config


@fixture(scope='session')
def app_config():
   cfg = Config()
   return cfg