const editButtons = document.getElementsByClassName("btn-edit");

const appointmentTitle = document.getElementById("id_title");
const appointmentStylist = document.getElementById("id_stylist");
const appointmentDateAppo = document.getElementById("id_date_appo");
const appointmentTimeAppo = document.getElementById("id_time_appo");

const appointmentForm = document.getElementById("appointmentForm");

const submitButton = document.getElementById("submitButton");


const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let appointmentId = e.target.getAttribute("data-appointment_id");
      let appointmentContent = document.getElementById(`appointment${appointmentId}`);

      appointmentTitle.value = appointmentContent.querySelector('.service-title').innerText;
      appointmentStylist.value = appointmentContent.querySelector('.stylist').innerText.split(': ')[1];
      appointmentDateAppo.value = appointmentContent.querySelector('.date').innerText.split(': ')[1];
      appointmentTimeAppo.value = appointmentContent.querySelector('.time').innerText.split(': ')[1];
      
      submitButton.innerText = "Update";
      appointmentForm.setAttribute("action", `/booking/edit_appointment/${appointmentId}/`);
    });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let appointmentId = e.target.getAttribute("data-appointment_id");
        deleteConfirm.href = `/booking/delete_appointment/${appointmentId}/`;
        
        deleteModal.show();
    });
}

