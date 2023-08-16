function printHello() {
    console.log('the javascript function ran!')
}

printHello()


// RESERVATION FORM

let formUrl = document.getElementById("form-url")
let newURL = formUrl.baseURI
console.log(newURL)

var date = newURL.slice(-10);
console.log(date)

let dateField = document.getElementById("id_date")
dateField.value = date

// dateField.style.display = "none"

let dateSection = document.getElementById("div_id_date")
dateSection.style.display = "none"