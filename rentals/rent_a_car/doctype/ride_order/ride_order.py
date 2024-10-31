# Copyright (c) 2024, ateeq and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RideOrder(Document):
    def before_save(self):
        ride_orders = frappe.get_all("Ride Order", fields=["name", "customer_name", "contact_no"])
        print(ride_orders)

        for order in ride_orders:
            contact_no = order.get("contact_no")
            customer_name = order.get("customer_name")
            existing_customer = frappe.db.exists("Customer Detail", {"contact_no": contact_no})            
            if not existing_customer:
                new_customer = frappe.new_doc("Customer Detail")
                new_customer.customer_name = customer_name
                new_customer.contact_no = contact_no
                print(contact_no)
                new_customer.insert()
                frappe.db.commit()
                
                print(f"New Customer created: {new_customer.customer_name}")
            else:
                print(f"Customer already exists: {customer_name}")
