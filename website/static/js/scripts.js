// function runTest() {
//     console.log('the javascript function ran!')
// }

// runTest()



//-------------RESERVATION FORM-------------

// AUTOFILL DATEFIELD
let formUrl = document.getElementById("form-url")
let newURL = formUrl.baseURI

var userDate = newURL.slice(-10);

let dateField = document.getElementById("id_date")
dateField.value = userDate


// GET RESERVATION LIST
let reservationList = document.getElementsByClassName("reservation-dates")


// CALCULATE COURT AVAILABILITY

console.log(`The user's chosen date is: ${userDate}`)

timeList = []

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
    let date = fullString.substr(0, 10);
    let timeslot = ""
    if (fullString.length > 14) {
        timeslot = fullString.slice(11,13)
    }
    else {
        timeslot = fullString.slice(11, 12)
    }
    if (date == userDate) {
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

// CONSOLE LOG THE TIME SLOT LISTS & COUNT RESERVATIONS
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
function AvailabilityCheck (timeslot) {
    let allTimes = document.getElementById("id_timeslot").children
    let targetTime = allTimes.item(timeslot + 1)

    if (reservationCount[timeslot] >= 9) {
        targetTime.disabled = true;
        targetTime.style.color = "red"
        targetTime.innerText += "-- Fully Booked"
    }
    else if (reservationCount[timeslot] >= 6) {
        targetTime.style.color = "orange"
        targetTime.innerHTML = `${targetTime.innerHTML} -- Limited Availability`
    }
}

for (let i = 0; i <= 11; i++) {
    AvailabilityCheck(i)
}

//AUTO COURT PICKER
let timeField = document.getElementById("id_timeslot")

timeField.addEventListener("change", pickCourt);

function pickCourt() {
    var timeField = document.getElementById("id_timeslot")
    var selectedTimeFull = timeField.options[timeField.selectedIndex].text;
    var selectedTime = selectedTimeFull.slice(0, 5)
    var bookings = 0
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

    let courtField = document.getElementById("id_court_number")
    courtField.value = parseInt(bookings)

    console.log(selectedTime)
    console.log(`There are ${bookings} reservations at that time`)
    console.log(`Therefore the reservation will be on Court ${bookings + 1}`)
}
