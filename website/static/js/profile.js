/* jshint esversion: 11 */
// PROFILE UPDATE

// Gets the update button and adds event listener
let editButton = document.getElementById('update-button');
editButton.addEventListener("click", showForm);

// Function to display the update form (hidden by default)
function showForm() {
    let updateForm = document.getElementById("update-form");
    updateForm.style.display = "block";
}

// Gets the cancel button and adds event listener
let cancelButton = document.getElementById("update-cancel-button");
cancelButton.addEventListener("click", hideForm);

// Function to hide the update form
function hideForm() {
    let updateForm = document.getElementById("update-form");
    updateForm.style.display = "none";
}