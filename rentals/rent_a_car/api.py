# rentals/rent_a_car/api.py
import frappe

@frappe.whitelist()
def get_vacant_vehicles():
    vehicles = frappe.get_all("Vehicle", fields=["id", "status", "title", "make"])
    vacant_vehicles = [
        {
            "id": vehicle["id"],
            "title": vehicle["title"],
            "make": vehicle["make"]
        }
        for vehicle in vehicles
        if vehicle["status"].strip().lower() in ["vacant", "vaccant"]
    ]
    return vacant_vehicles
