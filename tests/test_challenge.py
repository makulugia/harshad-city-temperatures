import unittest
from unittest import IsolatedAsyncioTestCase
import sys
# append the parent folder
sys.path.append('./')
from src.coding_challenge import runReport

# class TestChallenge(unittest.TestCase):
class TestChallenge(IsolatedAsyncioTestCase):
	async def test_san(self):
		global rr
		r1, r2, r3 = await runReport('San')
		self.assertTrue(r1.lower().find('san') != -1)
		self.assertTrue(r2.lower().find('san') != -1)
		self.assertGreater(len(r3),0)
	async def test_noresult(self):
		global rr
		r1, r2, r3 = await runReport('S')
		self.assertTrue(r1.lower().find('na') != -1)
		self.assertTrue(r2.lower().find('na') != -1)
		self.assertEqual(len(r3),0)
if __name__ == '__main__':
   unittest.main()
