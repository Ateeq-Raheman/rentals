// Copyright (c) 2024, ateeq and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    refresh(frm) {
        if (frm.doc.status === "Accepted") {
            frm.add_custom_button("Create Ride Booking", () => {
                frappe.new_doc('Ride Boking', {
                    order: frm.doc.name
                });
            });
        }

        if (frm.doc.status === "New" || (frm.doc.status !== "Accepted" && frm.doc.status !== "Rejected")) {
            frm.add_custom_button(
                "Accept", () => {
                    frm.set_value("status", "Accepted");
                    frm.save().then(() => {
                        frm.refresh();
                    });
                }, "Actions"
            );

            frm.add_custom_button(
                "Reject", () => {
                    frm.set_value("status", "Rejected");
                    frm.save().then(() => {
                        frm.refresh();
                    });
                }, "Actions"
            );
        }
    },
});

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

frappe.ui.form.on('Ride Order', {
    pickup_address: function (frm) {
        if (frm.doc.pickup_address) {
            if (frm.doc.items.length === 0) {
                frm.add_child("items");
            }
            frm.doc.items[0].source = frm.doc.pickup_address;
            frm.refresh_field("items");
        }
    }
});

frappe.ui.form.on('Ride Booking Item', {
    destination: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        let items = frm.doc.items;
        let index = items.findIndex(item => item.name === row.name);

        if (index >= 0 && index < items.length - 1) {
            items[index + 1].source = row.destination;
        } else if (index >= 0 && index === items.length - 1) {
            let new_row = frm.add_child("items");
            new_row.source = row.destination;
        }
        frm.refresh_field("items");
    }
});
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

frappe.ui.form.on("Ride Order", {
    before_save: function (frm) {
        if (frm.is_new() && !frm.doc.booking_time) {
            frm.set_value("booking_time", frappe.datetime.now_datetime());
        }
    }
});

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

frappe.ui.form.on('Ride Order Item', {
    destination: function (frm, cdt, cdn) {
        console.log("Destination function triggered for row:", cdn);
    }
});