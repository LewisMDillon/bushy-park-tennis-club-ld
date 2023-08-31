//-------------RESERVATION FORM-------------

// AUTOFILL DATEFIELD
// Gets the url of the form
let formUrl = document.getElementById("form-url")
let newURL = formUrl.baseURI


/*
Gets the last 10 characters of the url (this is the user's
chosen date in this format: YYYY-MM-DD)
*/
var userDate = newURL.slice(-10);

/*
Sets the hidden date input of the form to the
value of the user's chosen date
*/
let dateField = document.getElementById("id_date")
dateField.value = userDate


// GET RESERVATION LIST
// gets the data of all previous reservations
let reservationList = document.getElementsByClassName("reservation-dates")


// CALCULATE COURT AVAILABILITY

console.log(`The user's chosen date is: ${userDate}`) // delete this

/*
create empty list - will be a list of available timeslots
for the user to choose from
*/
timeList = []

/*
create 12 empty lists for timeslots - one
list for each timeslot on a given day 
*/
courtList0 = []
courtList1 = []
courtList2 = []
courtList3 = []
courtList4 = []
courtList5 = []
courtList6 = []
courtList7 = []
courtList8 = []
courtList9 = []
courtList10 = []
courtList11 = []

// SORT RESERVATIONS BY THEIR RESPECTIVE TIMESLOTS

for (let reservation of reservationList) {
    let fullString = reservation.innerText

    // extract the date and timeslot info from the data strings
    let date = fullString.substr(0, 10);
    let timeslot = ""

    // check for longer data strings due to double-digit timeslot number
    if (fullString.length > 14) {
        timeslot = fullString.slice(11,13)
    }
    else {
        timeslot = fullString.slice(11, 12)
    }

    // filter reservations by only those on user's chosen date
    if (date == userDate) {

        /*
        checks for bookings at all timeslots and adds an item to
        the respective courtList, for each booking at that timeslot
        */
        if (timeslot == "0") {
            courtList0.push(timeslot)
        }
        if (timeslot == "1") {
            courtList1.push(timeslot)
        }
        if (timeslot == "2") {
            courtList2.push(timeslot)
        }
        if (timeslot == "3") {
            courtList3.push(timeslot)
        }
        if (timeslot == "4") {
            courtList4.push(timeslot)
        }
        if (timeslot == "5") {
            courtList5.push(timeslot)
        }
        if (timeslot == "6") {
            courtList6.push(timeslot)
        }
        if (timeslot == "7") {
            courtList7.push(timeslot)
        }
        if (timeslot == "8") {
            courtList8.push(timeslot)
        }
        if (timeslot == "9") {
            courtList9.push(timeslot)
        }
        if (timeslot == "10") {
            courtList10.push(timeslot)
        }
        if (timeslot == "11") {
            courtList11.push(timeslot)
        }
    }
}

// CONSOLE LOG THE TIME SLOT LISTS & COUNT RESERVATIONS -- DELETE THIS
 console.log(`9:00 = ${courtList0} - ${courtList0.length} reservations`)
 console.log(`10:00 = ${courtList1} - ${courtList1.length} reservations`)
 console.log(`11:00 = ${courtList2} - ${courtList2.length} reservations`)
 console.log(`12:00 = ${courtList3} - ${courtList3.length} reservations`)
 console.log(`13:00 = ${courtList4} - ${courtList4.length} reservations`)
 console.log(`14:00 = ${courtList5} - ${courtList5.length} reservations`)
 console.log(`15:00 = ${courtList6} - ${courtList6.length} reservations`)
 console.log(`16:00 = ${courtList7} - ${courtList7.length} reservations`)
 console.log(`17:00 = ${courtList8} - ${courtList8.length} reservations`)
 console.log(`18:00 = ${courtList9} - ${courtList9.length} reservations`)
 console.log(`19:00 = ${courtList10} - ${courtList10.length} reservations`)
 console.log(`20:00 = ${courtList11} - ${courtList11.length} reservations`)

 
// Loop through the reservations and add all timeslot items to timeList
for (let reservation of reservationList) {
        let fullString = reservation.innerText
        let date = fullString.substr(0, 10);
        let timeslot = ""
        if (fullString.length > 14) {
            timeslot = fullString.slice(11,13)
        }
        else {
            timeslot = fullString.slice(11, 12)
        }
        if (date == userDate) {
            timeList.push(timeslot);
        }
    }

// Count the reservations in each timeslot
let reservationCount = timeList.reduce(function (
    count,
    currentValue
) {
    return (
        count[currentValue] ? ++count[currentValue] : (count[currentValue] = 1),
        count
    );
},
{});


// AVAILABILITY CHECKER
/*
Disables fully booked timeslots (timeslots with 9 existing bookings)
Adds 'limited availability' styling to busy timeslots (6 to 8 bookings)
*/
function AvailabilityCheck (timeslot) {

    // get the timeslot input field
    let allTimes = document.getElementById("id_timeslot").children
    let targetTime = allTimes.item(timeslot + 1)

    // disables fully booked timeslots
    if (reservationCount[timeslot] >= 9) {
        targetTime.disabled = true;
        targetTime.style.color = "red"
        targetTime.innerText += " -- Fully Booked "
    }

    // adds styling to busy timeslots
    else if (reservationCount[timeslot] >= 6) {
        targetTime.style.color = "orange"
        targetTime.innerHTML = `${targetTime.innerHTML} -- Limited Availability `
    }
}

// Runs availability check for each timeslot
for (let i = 0; i <= 11; i++) {
    AvailabilityCheck(i)
}

//AUTO COURT PICKER
/*
Automatically selects the next available court
based on the amount of existing bookings
*/

// Get the timeslot input field and add event listener
let timeField = document.getElementById("id_timeslot")
timeField.addEventListener("change", pickCourt);

function pickCourt() {
    var timeField = document.getElementById("id_timeslot")

    // Get a string of the user's selected time
    var selectedTimeFull = timeField.options[timeField.selectedIndex].text;
    var selectedTime = selectedTimeFull.slice(0, 5)

    // create bookings variable to store number of bookings at each timeslot
    var bookings = 0

    // assigns value to bookings variable based on user choice
    if (selectedTime == "09:00") {
        bookings = courtList0.length
    }
    if (selectedTime == "10:00") {
        bookings = courtList1.length
    }
    if (selectedTime == "11:00") {
        bookings = courtList2.length
    }
    if (selectedTime == "12:00") {
        bookings = courtList3.length
    }
    if (selectedTime == "13:00") {
        bookings = courtList4.length
    }
    if (selectedTime == "14:00") {
        bookings = courtList5.length
    }
    if (selectedTime == "15:00") {
        bookings = courtList6.length
    }
    if (selectedTime == "16:00") {
        bookings = courtList7.length
    }
    if (selectedTime == "17:00") {
        bookings = courtList8.length
    }
    if (selectedTime == "18:00") {
        bookings = courtList9.length
    }
    if (selectedTime == "19:00") {
        bookings = courtList10.length
    }
    if (selectedTime == "20:00") {
        bookings = courtList11.length
    }

    // get the hidden court_number input field and assign it the value of bookings
    let courtField = document.getElementById("id_court_number")
    courtField.value = parseInt(bookings) // don't need (bookings + 1) here since court numbers begin at 0

    console.log(selectedTime)
    console.log(`There are ${bookings} reservations at that time`)
    console.log(`Therefore the reservation will be on Court ${bookings + 1}`)
}
