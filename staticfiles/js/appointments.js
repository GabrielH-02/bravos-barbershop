/* Variable for editorial functionality */
const editButtons = document.getElementsByClassName("btn-edit");

/* Variables for the editorial functionality; each for the data fields of the appointment form */
const appointmentTitle = document.getElementById("id_title");
const appointmentStylist = document.getElementById("id_stylist");
const appointmentDateAppo = document.getElementById("id_date_appo");
const appointmentTimeAppo = document.getElementById("id_time_appo");
const appointmentForm = document.getElementById("appointmentForm");
const submitButton = document.getElementById("submitButton");

/* Variables of the deletion functionality */
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


/* Function for the editoriial of appointments */

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated appointment's ID upon click.
 * - Fetches the content of the corresponding appointment.
 * - Populates the appointment form fields with the appointment's details for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_appointment/{appointmentId}` endpoint.
 */

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let appointmentId = e.target.getAttribute("data-appointment_id");
        let appointmentContent = document.getElementById(`appointment${appointmentId}`);

        appointmentTitle.value = appointmentContent.querySelector('.service-title').innerText;
        appointmentStylist.value = appointmentContent.querySelector('.stylist').innerText.split(': ')[1];
        appointmentDateAppo.value = appointmentContent.querySelector('.date').innerText.split(': ')[1];
        appointmentTimeAppo.value = appointmentContent.querySelector('.time').innerText;

        submitButton.innerText = "Update";
        appointmentForm.setAttribute("action", `/booking/edit_appointment/${appointmentId}/`);
    });
}

/* Function for the deletion of appointments */

/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated appointment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 *   deletion endpoint for the specific appointment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 *   the user for confirmation before deletion.
 */

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let appointmentId = e.target.getAttribute("data-appointment_id");
        deleteConfirm.href = `/booking/delete_appointment/${appointmentId}/`;

        deleteModal.show();
    });
}
