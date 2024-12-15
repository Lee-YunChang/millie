from contextlib import contextmanager
from typing import Callable

from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_409_CONFLICT,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_429_TOO_MANY_REQUESTS,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE,
)

from utils.exceptions import (
    DecodeError,
)
from utils.response import APIResponse


class AssertionMixin:
    '''
    Mixin for assertion helpers
    '''
    assertEqual: Callable

    def assertOK(self, response, *, code=None):
        self.assertEqual(response.status_code, HTTP_200_OK, response.data)
        if code:
            self.assertEqual(response.data['code'], code, response.data)

    def assertCreated(self, response):
        self.assertEqual(response.status_code, HTTP_201_CREATED, response.data)

    def assertAccepted(self, response):
        self.assertEqual(response.status_code, HTTP_202_ACCEPTED, response.data)

    def assertNoContent(self, response):
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT, response.data)

    def assertBadRequest(self, response, code='BAD_REQUEST'):
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST, response.data)
        self.assertEqual(response.data['error']['code'], code, response.data)

    def assertTooManyRequest(self, response, code='TOO_MANY_REQUESTS'):
        self.assertEqual(response.status_code, HTTP_429_TOO_MANY_REQUESTS, response.data)
        self.assertEqual(response.data['error']['code'], code, response.data)

    def assertUnauthorized(self, response):
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED, response.data)

    def assertForbidden(self, response):
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN, response.data)

    def assertInvalidParam(self, response):
        self.assertBadRequest(response, APIResponse.Code.INVALID_PARAM.value)

    def assertNotFound(self, response, expected_code='NOT_FOUND'):
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND, response.data)
        self.assertEqual(response.data['error']['code'], expected_code, response.data)

    def assertConflict(self, response, expected_code='CONFLICT'):
        self.assertEqual(response.status_code, HTTP_409_CONFLICT, response.data)
        self.assertEqual(response.data['error']['code'], expected_code, response.data)

    def assertInvalidState(self, response):
        self.assertUnprocessableEntity(response, APIResponse.Code.INVALID_STATE.value)

    def assertInsufficientFunds(self, response):
        self.assertUnprocessableEntity(response, APIResponse.Code.INSUFFICIENT_FUNDS.value)

    def assertInvalidSignUpStatus(self, response):
        self.assertUnprocessableEntity(response, 'INVALID_SIGNUP_STATUS')

    def assertDecodeError(self, response, expected_code=DecodeError.code):
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST, response.data)
        self.assertEqual(response.data['error']['code'], expected_code, response.data)
    @contextmanager
    def assertFreezeBalance(self, account, amount):
        account.refresh_from_db()
        original_frozen = account.frozen_balance
        original_unfrozen = account.unfrozen_balance
        yield

        account.refresh_from_db()
        self.assertEqual(original_frozen + amount, account.frozen_balance, 'Unexpected frozen_balance')
        self.assertEqual(original_unfrozen - amount, account.unfrozen_balance, 'Unexpected unfrozen_balance')

    @contextmanager
    def assertDebitFrozenBalance(self, account, amount):
        account.refresh_from_db()
        original_frozen = account.frozen_balance
        yield

        account.refresh_from_db()
        self.assertEqual(original_frozen - amount, account.frozen_balance, 'Unexpected frozen_balance')

    @contextmanager
    def assertUnfreezeBalance(self, account, amount):
        account.refresh_from_db()
        original_frozen = account.frozen_balance
        original_unfrozen = account.unfrozen_balance
        yield

        account.refresh_from_db()
        self.assertEqual(original_frozen - amount, account.frozen_balance, 'Unexpected frozen_balance')
        self.assertEqual(original_unfrozen + amount, account.unfrozen_balance, 'Unexpected unfrozen_balance')

    @contextmanager
    def assertRefund(self, account, amount):
        account.refresh_from_db()
        original_unfrozen = account.unfrozen_balance
        yield

        account.refresh_from_db()
        self.assertEqual(original_unfrozen + amount, account.unfrozen_balance, 'Unexpected unfrozen_balance')
