import string
import time
from collections import defaultdict
from random import choice
from types import SimpleNamespace
from unittest import TextTestResult
from unittest.mock import (
    MagicMock,
    patch,
)

from django.conf import settings
from django.test import (
    modify_settings,
    override_settings,
)
from django.test.runner import DiscoverRunner


class MockBucket:
    def put_object(self, **kwargs):
        o = SimpleNamespace()
        o.version_id = ''.join(choice(string.ascii_letters + string.digits) for _ in range(64))
        return o


class TimeTextTestResult(TextTestResult):
    """
    Inherits TextTestResult class. Overrides startTest, addSuccess functions
    to time the unittests. Stores tests that take longer than 0.2 sec in slow_test
    dict.
    """
    slow_tests = {}
    slow_test_classes = defaultdict(float)

    def startTest(self, test):
        """
        테스트 시작: 시간 기록
        """
        super().startTest(test)
        self.started_at = time.time()

    def addSuccess(self, test):
        """
        테스트 성공시:
        1. function 단위의 테스트 시간 기록 (slow_tests)
        2. 클래스 단위의 테스트 시간 기록 (slow_test_classes)
        """
        super().addSuccess(test)
        self.time_taken = time.time() - self.started_at

        # str(test) format: {test function name}({test class name})
        test_name = str(test)
        test_class = test_name.split('(')[1][:-1]
        self.slow_test_classes[test_class] += self.time_taken
        if self.time_taken > settings.SLOW_TEST_THRESHOLD:
            self.slow_tests[test_name] = self.time_taken

    def stopTestRun(self):
        """
        모든 테스트 종류 후 가장 느린 테스트와 테스트 클래스를 출력.
        """
        number_of_slowtests = slice(0, settings.NUMBER_OF_SLOW_TESTS_TO_PRINT)
        number_of_slowclasses = slice(0, settings.NUMBER_OF_SLOW_TEST_CLASSES_TO_PRINT)
        slow_classes = sorted(self.slow_test_classes.items(), key=lambda kv: kv[1], reverse=True)[number_of_slowclasses]
        slow_tests = sorted(self.slow_tests.items(), key=lambda kv: kv[1], reverse=True)[number_of_slowtests]
        print("\nThese are the slowest test classes.")

        for slow_test_class in slow_classes:
            print(f"\nTest class name: {slow_test_class[0]} \nTest Time: {slow_test_class[1]:.3f}s\n")

        print(f"\nThere are {len(self.slow_tests)} tests that take longer than {settings.SLOW_TEST_THRESHOLD}.")

        for slow_test in slow_tests:
            print(f"Test name: {slow_test[0]} \nTest Time: {slow_test[1]:.3f}s\n")


class UnitTestRunner(DiscoverRunner):

    @patch('utils.file._is_file_mime_type', lambda *args: True)
    @patch('geoip2.database.Reader', MagicMock())
    # To prevent temporary files created in tests from being saved
    @patch('django.core.files.storage.FileSystemStorage.save', return_value='filename')
    @override_settings(MOCK_BANK_ENABLED=True)
    @override_settings(HANA_BANK_HOST="TEST")
    @override_settings(STAFF_OTP_ENABLED=False)
    @override_settings(ALLOW_TO_SUBSCRIBE_ON_WEEKEND=True)
    @override_settings(SUBSCRIPTION_LIMIT_IN_PERCENT=5.0)
    @override_settings(PAGERDUTY_OFFERING_RAISED_CAPITAL_RECONCILIATION_ENABLED=False)
    @modify_settings(MIDDLEWARE={
        'remove': 'utils.middlewares.BlockingApiMiddleware',
    })
    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        return super().run_tests(test_labels, extra_tests=None, **kwargs)

    def get_resultclass(self):
        """
        Override get_resultclass to time the unittests when
        TIME_UNITTESTS is set to True.
        """
        if settings.TEST_TIME_MEASUREMENT_ENABLED:
            return TimeTextTestResult
        return super().get_resultclass()
