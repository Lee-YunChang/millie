from rest_framework.test import APITestCase


class FixtureMixin:
    fixtures = ['millie/services/fixtures.yaml']


class FixturedAPITestCase(FixtureMixin, APITestCase):
    '''
    A simple TestCase with fixture.
    '''
    pass
