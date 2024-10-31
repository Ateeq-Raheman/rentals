# Copyright (c) 2024, ateeq and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestDriver(FrappeTestCase):
	def test_full_name_correctly_set(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name = "Driver"
		test_driver.last_name = "adalslclmclvd"
		test_driver.licence_number = "wqddandskand"
		test_driver.save()

		self.assertEqual(test_driver.full_name, "Driver adalslclmclvd")

	def test_full_name_correctly_set_when_last_name_not_set(self):
		test_driver = frappe.new_doc("Driver")
		test_driver.first_name = "Driver"
		test_driver.licence_number = "wqddandskand"
		test_driver.save()

		self.assertEqual(test_driver.full_name, "Driver")