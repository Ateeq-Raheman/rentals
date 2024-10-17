// Copyright (c) 2024, ateeq and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Boking", {
    refresh(frm) {

    },
    rate(frm) {
        frm.trigger("update_total_amount")
    },
    update_total_amount(frm) {
        let total_d = 0
        for (let i of frm.doc.items) {
            total_d += i.distance
        }

        const total = frm.doc.rate * total_d
        frm.set_value("total_amount", total);
    }
});
frappe.ui.form.on("Ride Booking Item", {
    distance(frm, cdt, cdn) {
        frm.trigger("update_total_amount")
    },
    items_remove(frm) {
        frm.trigger("update_total_amount")

    },
    items_add(frm) {
        frm.trigger("update_total_amount")
    }
})
