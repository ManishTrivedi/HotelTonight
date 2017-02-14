from django.test import TestCase
from casedata.utils import *
from casedata.models import Case

class UtilTestCase(TestCase):

	def test_open_status(self):
		self.assertEqual(format_status('open'), 'Open')

	def test_closed_status(self):
		self.assertEqual(format_status('closed'), 'Closed')

	def test_invalid_status(self):
		self.assertEqual(format_status('pending'), None)	

	def test_from_date(self):
		from_time='2017-02-10 00:00:00.000000'
		self.assertEqual(format_datetime(1486684800)[0], from_time)

	def test_filters_for_empty_parameters(self):
		params = {}
		self.assertIsNotNone(get_filters_from_query_string(params))

	def test_status_filter(self):
		params = { 'status' : 'open' }
		filters = get_filters_from_query_string(params)
		self.assertIsNotNone(filters)
		self.assertIsNotNone(filters.get('status', None))

	def test_category_filter(self):
		params = { 'category' : 'default' }
		filters = get_filters_from_query_string(params)
		self.assertIsNotNone(filters)
		self.assertIsNotNone(filters.get('category', None))

	def test_since_filter(self):
		params = { 'since' : '1486684800' }
		filters = get_filters_from_query_string(params)
		self.assertIsNotNone(filters)
		self.assertIsNotNone(filters.get('opened__range', None))

	def test_empty_status_filter(self):
		params = {}
		filters = get_filters_from_query_string(params)
		self.assertIsNotNone(filters)
		self.assertIsNone(filters.get('status', None))

	def test_empty_category_filter(self):
		params = {}
		filters = get_filters_from_query_string(params)
		self.assertIsNotNone(filters)
		self.assertIsNone(filters.get('category', None))

	def test_empty_since_filter(self):
		params = {}
		filters = get_filters_from_query_string(params)
		self.assertIsNotNone(filters)
		self.assertIsNone(filters.get('opened__range', None))

	def test_get_cases_api(self):
		response = self.client.get('/cases/')
		self.assertEqual(response.status_code, 200)	

		

