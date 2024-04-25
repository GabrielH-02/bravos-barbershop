const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let appointmentId = e.target.getAttribute("data-appointment_id");
        deleteConfirm.href = `/booking/delete_appointment/${appointmentId}/`;
        
        deleteModal.show();
    });
}