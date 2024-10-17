// Copyright (c) 2024, ateeq and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle", {
    refresh(frm) {

    },
    get_summary(frm) {
        frm.get_field("summary").$wrapper.append("<h1>Hello</h1>")
    }
});
