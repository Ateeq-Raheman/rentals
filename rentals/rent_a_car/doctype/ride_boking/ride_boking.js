// Copyright (c) 2024, ateeq and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Boking", {
    rate(frm) {
        frm.trigger("update_total_amount")
    },

    order(frm) {
        frappe.call({
            method: 'frappe.client.get',
            args: {
                doctype: "Ride Order",
                name: frm.doc.order
            },
            callback: function (r) {
                if (r.message) {
                    const items = r.message.items
                    items.forEach(item => {
                        frm.add_child("items", {
                            source: item.source,
                            destination: item.destination,
                            distance: item.distance,
                        })

                    });
                    frm.refresh_field('items');
                    third(frm)
                }
            }
        });
    },
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

frappe.ui.form.on('Ride Booking', {
    onload: function (frm) {
        frm.set_query('order', function () {
            return {
                filters: {
                    'status': ['!=', Completed],
                    'status': ['=',]
                }
            };
        });
    }
});

function update_total_amount(frm, rent, rent_1, rent_2) {
    let total_d = 0
    frm.doc.items.forEach(
        (row) => {
            total_d += row.distance
            console.log("middle")
        }
    )
    frm.set_value("total_distance", total_d)
    second(frm, rent, rent_1, rent_2)
    console.log("last")

}

function second(frm, rent, rent_1, rent_2) {
    if (frm.doc.total_distance <= 10) {
        frm.set_value("rate", rent);
    } else if (frm.doc.total_distance > 10 && frm.doc.total_distance < 20) {
        frm.set_value("rate", rent_1);
    } else if (frm.doc.total_distance >= 20) {
        frm.set_value("rate", rent_2);
    }
    const total = frm.doc.rate * frm.doc.total_distance;
    frm.set_value("total_amount", total);
}
function third(frm) {
    frappe.call({
        method: 'frappe.client.get',
        args: {
            doctype: "Rentals Settings"
        },
        callback: function (r) {
            if (r.message) {
                console.log(r.message)
                const rent = r.message.less_then_10km
                const rent_1 = r.message.between_10_to_20_km
                const rent_2 = r.message.above_20_km
                update_total_amount(frm, rent, rent_1, rent_2)
                console.log(rent)
                console.log(rent_1)
                console.log(rent_2)
            }
        }
    });
}

frappe.ui.form.on("Ride Boking", {
    order: function () {
        if (frm.doc.order) {
            frappe.db.get_doc("Ride Order", fr.doc.order).then(doc => {
                frm.set_value("pickup_time", doc.pickup_time);
            })
        }
    }
})

frappe.ui.form.on("Ride Boking", {
    rate: function () {
        if (frm.doc.rate) {
            frm.doc.total_amount = frm.doc.rate * frm.doc.total_distance
        }
    }
})
