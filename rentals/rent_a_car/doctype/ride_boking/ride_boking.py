# Copyright (c) 2024, ateeq and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


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


    # def before_save(self):
    #     if self.rate:
    #         self.total_amount = self.total_distance * self.rate

