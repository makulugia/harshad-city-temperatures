import pytest
import unittest
import asyncio
import sys
# append the parent folder
sys.path.append('./')
from src.coding_challenge import runReport

@pytest.fixture(scope="class")
def event_loop_instance(request):
    """ Add the event_loop as an attribute to the unittest style test class. """
    request.cls.event_loop = asyncio.get_event_loop_policy().new_event_loop()
    yield
    request.cls.event_loop.close()

@pytest.mark.usefixtures("event_loop_instance")
class TestTheThings(unittest.TestCase):

    def get_async_result(self, coro):
        """ Run a coroutine synchronously. """
        return self.event_loop.run_until_complete(coro)

    def test_an_async_method(self):
        r1, r2, r3 = self.get_async_result(runReport('San'))
        # result is the actual result, so whatever assertions..
        self.assertTrue(r1.lower().find('san') != -1)
        self.assertTrue(r2.lower().find('san') != -1)
        self.assertGreater(len(r3),0)
