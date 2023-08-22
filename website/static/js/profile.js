// PROFILE UPDATE

let editButton = document.getElementById('update-button')

editButton.addEventListener("click", showForm)

function showForm() {
    let updateForm = document.getElementById("update-form")
    updateForm.style.display = "block"
}

let cancelButton = document.getElementById("update-cancel-button")

cancelButton.addEventListener("click", hideForm)

function hideForm() {
    let updateForm = document.getElementById("update-form")
    updateForm.style.display = "none"
}