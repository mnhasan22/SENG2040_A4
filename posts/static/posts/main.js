// Filename         : main.js
// Project          : SENG2040 Assignment 4
// By               : Md Nazmul Hasan (8938868)
// Date             : March 25, 2025
// Description      : This file contains the JavaScript code for handling appointment 
//                    form submission and displaying appointments on the page.
// document.addEventListener('DOMContentLoaded', () => {
//     fetchAppointments();

//     document.getElementById('appointmentForm').addEventListener('submit', async (e) => {
//         e.preventDefault();

//         const data = {
//             student_name: document.getElementById('studentName').value,
//             email: document.getElementById('email').value,
//             purpose: document.getElementById('purpose').value,
//             preferred_date: document.getElementById('preferredDate').value,
//             status: 'Pending'
//         };

//         const response = await fetch('/api/appointments/', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify(data)
//         });

//         if (response.ok) {
//             fetchAppointments();
//             e.target.reset();
//             alert('Appointment request submitted!');
//         } else {
//             alert('Failed to submit appointment. Try again.');
//         }
//     });
// });

// async function fetchAppointments() {
//     const response = await fetch('/api/appointments/');
//     const appointments = await response.json();

//     const container = document.getElementById('appointments');
//     container.innerHTML = '';

//     appointments.forEach(app => {
//         const col = document.createElement('div');
//         col.className = 'col-md-6 col-lg-4';

//         col.innerHTML = `
//             <div class="card shadow-sm h-100">
//                 <div class="card-body">
//                     <h5 class="card-title">${app.student_name}</h5>
//                     <h6 class="card-subtitle mb-2 text-muted">${app.email}</h6>
//                     <p class="card-text"><strong>Purpose:</strong> ${app.purpose}</p>
//                     <p class="card-text"><strong>Date:</strong> ${new Date(app.preferred_date).toLocaleString()}</p>
//                     <span class="badge ${
//                         app.status === 'Approved' ? 'bg-success' :
//                         app.status === 'Declined' ? 'bg-danger' : 'bg-warning text-dark'
//                     }">${app.status}</span>
//                 </div>
//             </div>
//         `;

//         container.appendChild(col);
//     });
// }

document.addEventListener('DOMContentLoaded', () => {
    fetchAppointments();

    const form = document.getElementById('appointmentForm');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        formData.append('status', 'Pending');

        const response = await fetch('/api/appointments/', {
            method: 'POST',
            body: formData
        });

        const msgBox = document.getElementById('message');
        if (response.ok) {
            form.reset();
            fetchAppointments();
            msgBox.innerHTML = `<div class="alert alert-success">Appointment submitted successfully!</div>`;
        } else {
            msgBox.innerHTML = `<div class="alert alert-danger">Failed to submit. Try again later.</div>`;
        }
    });
});

async function fetchAppointments() {
    const response = await fetch('/api/appointments/');
    const appointments = await response.json();

    const container = document.getElementById('appointments');
    container.innerHTML = '';

    appointments.forEach(app => {
        const col = document.createElement('div');
        col.className = 'col-md-6 col-lg-4';

        col.innerHTML = `
            <div class="card shadow-sm h-100">
                <div class="card-body">
                    <h5 class="card-title">${app.student_name} (${app.student_id})</h5>
                    <h6 class="card-subtitle mb-2 text-muted">${app.email}</h6>
                    <p class="card-text"><strong>Purpose:</strong> ${app.purpose}</p>
                    <p class="card-text"><strong>Date:</strong> ${new Date(app.preferred_date).toLocaleString()}</p>
                    ${app.attachment ? `<p><a href="${app.attachment}" target="_blank">View Attachment</a></p>` : ''}
                    <span class="badge ${
                        app.status === 'Approved' ? 'bg-success' :
                        app.status === 'Declined' ? 'bg-danger' : 'bg-warning text-dark'
                    }">${app.status}</span>
                </div>
            </div>
        `;

        container.appendChild(col);
    });
}
