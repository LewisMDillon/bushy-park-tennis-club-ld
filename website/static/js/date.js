// DATE PICKER 

// Gets date info for formatting
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1; // January is 0
var yyyy = today.getFullYear();

if (dd < 10) {
   dd = '0' + dd;
}

if (mm < 10) {
   mm = '0' + mm;
} 

// Formats the date
today = yyyy + '-' + mm + '-' + dd;

// Disables selection of dates before the present day
document.getElementById("date-picker").setAttribute("min", today);
