# Copyright (c) 2024, ateeq and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import now_datetime
from datetime import timedelta
class RideBoking(Document):
    def validate(self):
        if self.workflow_state == "Approved":
            rideorder = frappe.get_doc("Ride Order", self.order)
            rideorder.status = "Completed"
            rideorder.save()
            vehicle = frappe.get_doc("Vehicle", self.vehicle)
            vehicle.status = "occupied"
            vehicle.save()
            driver = frappe.get_doc("Driver", self.driver)
            driver.status = "Occupied"
            driver.save()
            frappe.errprint("status has been set")
        else:
            driver = frappe.get_doc("Driver", self.driver)
            driver.status = "Vaccant"
            driver.save()
            vehicle = frappe.get_doc("Vehicle",self.vehicle)
            vehicle.status = "vaccant"
            vehicle.save()
def before_save(self):
    # Check if pickup_time is set to avoid errors
    if self.pickup_time:
        # Set Expected Time by adding 60 minutes to pickup_time
        self.expected_time = self.pickup_time + timedelta(minutes=60)



def check_and_update_ride_status():
    bookings = frappe.get_all('Ride Boking', filters={'workflow_state': 'Approved'}, fields=['name', 'expected_time', 'pickup_time'])
    for booking in bookings:
        # Convert pickup_time to a datetime object if it's a string (for consistency)
        pickup_time = booking['pickup_time']
        if isinstance(pickup_time, str):
            pickup_time = datetime.strptime(pickup_time, "%Y-%m-%d %H:%M:%S")

        # Ensure expected_time is a datetime object
        expected_time = booking['expected_time']
        if isinstance(expected_time, str):
            expected_time = datetime.strptime(expected_time, "%Y-%m-%d %H:%M:%S")

        # Compare now with expected_time directly
        if now_datetime() > expected_time:
            frappe.msgprint(f"Booking {booking['name']} - Condition met for Auto Failed status.")
            doc = frappe.get_doc('Ride Boking', booking['name'])
            doc.workflow_state = 'Auto Failed'
            doc.save()
            frappe.db.commit()
            frappe.msgprint(f"Booking {booking['name']} - Status updated to Auto Failed")
        else:
            frappe.msgprint(f"Booking {booking['name']} - Condition NOT met for Auto Failed status.")

