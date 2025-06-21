// This script adds an event listener to the "Add Employee" button

document.addEventListener('DOMContentLoaded', function () {
    const addEmployeeBtn = document.getElementById('addEmployee');
    if (addEmployeeBtn) {
        addEmployeeBtn.addEventListener('click', function () {
            window.location.href = '/addemployee.html';
        });
    }
});