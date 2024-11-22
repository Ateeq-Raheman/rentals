frappe.ui.form.on("vehicle", {
    refresh: function (frm) {
        // Add a custom button below or near the identified class
        const targetElement = document.querySelector("button.btn-reset.nav-link");

        if (targetElement) {
            // Create a new button element
            const newButton = document.createElement("button");
            newButton.innerText = "Translate to Urdu";
            newButton.className = "btn btn-primary custom-button";
            newButton.style.marginLeft = "10px"; // Adjust position relative to the original button

            // Attach a click event to the button
            newButton.onclick = function () {
                frappe.msgprint(__('Translate to Urdu button clicked!'));
            };

            // Append the new button after the target element
            targetElement.parentNode.insertBefore(newButton, targetElement.nextSibling);
            console.log("Custom button added near 'Save' area.");
        } else {
            console.error("Target element not found.");
        }
    },
});
