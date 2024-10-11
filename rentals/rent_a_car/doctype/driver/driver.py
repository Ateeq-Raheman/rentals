# Copyright (c) 2024, ateeq and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	def before_save(self):
		if not self.full_name:
			self.full_name = self.first_name + " " + self.last_name

	def send_alert(self):{
		print("sending meassage")
	}