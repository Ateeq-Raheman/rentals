# Copyright (c) 2024, ateeq and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import now_datetime , time_diff_in_seconds
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
    print(bookings)
    for booking in bookings:
        print(booking)
        pickup_time = booking.pickup_time
        expected_time = float(booking.expected_time)
        current_time = now_datetime()
        diff_in_seconds = time_diff_in_seconds(current_time,pickup_time)
        diff_in_minutes = diff_in_seconds / 60
        if(diff_in_minutes > expected_time):
            doc = frappe.get_doc('Ride Boking', booking['name'])
            doc.add_comment("Comment", "Automatically transitioning to Auto Failed due to exceeded expected time.")
            doc.workflow_state = "Auto Failed"  # Replace 'failed' with the actual action name for the transition
            doc.save(ignore_permissions=True)
            frappe.db.commit()

# frappe.ui.form.on('Student Learning Status', { refresh: function (frm) { // Attach functionality to the "create a daily progress" button frm.fields_dict.create_a_daily_progress.$wrapper.on('click', function () { // Call the server-side create_weekly_progress method frappe.call({ method: "shaheen_dev.api.custom_api.create_weekly_progress", args: { student_id: frm.doc.student_id }, callback: function (response) { if (response.message && response.message.status === "success") { const uncheckedFields = response.message.unchecked_fields; const previouslyCheckedFields = response.message.previously_checked_fields; const studentId = response.message.student_id; if (uncheckedFields.length > 0) { const dialogFields = uncheckedFields.map(field => ({ label: field.replace(/_/g, ' '), // Replace underscores with spaces fieldname: field, fieldtype: 'Check' })); const dialog = new frappe.ui.Dialog({ title: 'Select Fields to Save', fields: dialogFields, primary_action_label: 'Save', primary_action(values) { const mergedFields = { ...previouslyCheckedFields, ...values }; // Save progress via the save_weekly_progress server method frappe.call({ method: "shaheen_dev.api.custom_api.save_weekly_progress", args: { student_id: studentId, field_data: JSON.stringify(mergedFields) // Convert merged fields to JSON }, callback: function (saveResponse) { if (saveResponse.message && saveResponse.message.status === "success") { frappe.msgprint(__('Progress created and saved successfully!')); dialog.hide(); } else { frappe.msgprint(__('Failed to save progress: ') + saveResponse.message.message); } }, error: function () { frappe.msgprint(__('Failed to save progress.')); } }); } }); dialog.show(); } else { frappe.msgprint(__('No unchecked fields available for this student.')); } } else { frappe.msgprint(__('Failed to retrieve unchecked fields or an error occurred.')); } }, error: function () { frappe.msgprint(__('Failed to call the server script.')); } }); }); } });
