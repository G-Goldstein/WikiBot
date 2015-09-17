import unittest
import src.page_categorisation as Categoriser
from mock import patch, MagicMock

class TestWikiInit(unittest.TestCase):

	def test_propertyValueString(self):
		prop = 'Colour'
		val = 'Red'
		propVal = 'Colour=Red'
		self.assertEqual(Categoriser.propertyValueString(prop,val),propVal)

	def test_templateTextToAdd(self):
		area = 'TRDI'
		expectation = '{{Page ownership|area=TRDI|review=yes}}'
		self.assertEqual(Categoriser.templateTextToAdd(area), expectation)


if __name__ == '__main__':
	unittest.main()