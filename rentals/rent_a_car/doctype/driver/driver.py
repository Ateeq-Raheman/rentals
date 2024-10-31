# Copyright (c) 2024, ateeq and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Driver(Document):
	def before_save(self):
		if not self.full_name:
			self.full_name = f"{self.first_name} {self.last_name}"
		else:
			self.last_name = self.first_name

	# def update_driver_status(self):
	# 	driver = frappe.get_doc("Driver")
	# 	ride_booking = frappe.get_doc("Ride Booking")
	# 	if self.ride_booking == "completed":
	# 		frappe.frappe.db.set_value('Driver', 'status',"Vaccant" )
	# 	else:
	# 		frappe.db.set_value('Driver', 'status', "Occupied")



	def send_alert(self):{
		print("sending meassage")
	}