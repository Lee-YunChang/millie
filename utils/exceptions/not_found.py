from typing import Type

from django.db import models
from rest_framework import status

from utils.exceptions import MillieAPIException


class NotFoundError(MillieAPIException):
    status_code = status.HTTP_404_NOT_FOUND
    message = 'Not found.'
    code = 'NOT_FOUND'


class ObjectNotFoundError(NotFoundError):
    message = 'Object not found.'
    code = 'NOT_FOUND'

    def __init__(self, model: Type[models.Model], *args, **kwargs):
        if not kwargs.get('message'):
            kwargs['message'] = f"{model.__name__} object not found."
        super().__init__(*args, **kwargs)


class InvalidUUIDError(NotFoundError):
    title = 'Invalid uuid'
    message = 'Invalid uuid'
    description = 'uuid 형식이 올바르지 않습니다.'
