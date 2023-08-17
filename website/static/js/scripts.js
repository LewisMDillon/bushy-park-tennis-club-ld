function printHello() {
    console.log('the javascript function ran!')
}

printHello()



//-------------RESERVATION FORM-------------

// AUTOFILL DATE & HIDE DATEFIELD
let formUrl = document.getElementById("form-url")
let newURL = formUrl.baseURI
console.log(newURL)

var userDate = newURL.slice(-10);
console.log(userDate)

let dateField = document.getElementById("id_date")
dateField.value = userDate

let dateSection = document.getElementById("div_id_date")
dateSection.style.display = "none"


// GET RESERVATION LIST
let reservationList = document.getElementsByClassName("reservation-dates")

// HIDE RESERVATION LIST
// for (let reservation of reservationList) {
//     reservation.style.display = 'none';
//     }

// CALCULATE COURT AVAILABILITY
console.log("below is the userDate")
console.log(userDate)

timeList = []
courtList = []

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

for (let reservation of reservationList) {
    let fullString = reservation.innerText
    let date = fullString.substr(0, 10);
    let timeslot = fullString.slice(11, 12)
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
 console.log(`courtList0 = ${courtList0}`)
 console.log(`courtList1 = ${courtList1}`)
 console.log(`courtList2 = ${courtList2}`)
 console.log(`courtList3 = ${courtList3}`)
 console.log(`courtList4 = ${courtList4}`)
 console.log(`courtList5 = ${courtList5}`)
 console.log(`courtList6 = ${courtList6}`)
 console.log(`courtList7 = ${courtList7}`)
 console.log(`courtList8 = ${courtList8}`)
 console.log(`courtList9 = ${courtList9}`)
 console.log(`courtList10 = ${courtList10}`)
 console.log(`courtList11 = ${courtList11}`)

for (let reservation of reservationList) {
        let fullString = reservation.innerText
        let date = fullString.substr(0, 10);
        let timeslot = fullString.slice(11, 12)
        let court = fullString.slice(fullString.length - 1)
        if (date == userDate) {
            timeList.push(timeslot);
            courtList.push(court)
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


// TIMESLOT CHECKER
function AvailabilityCheck (timeslot) {
    let allTimes = document.getElementById("id_timeslot").children
    let targetTime = allTimes.item(timeslot + 1)
    let courtField = document.getElementById("id_court_number")

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

//COURT PICKER
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
        let bookings = courtList2.length
    }
    if (selectedTime == "12:00") {
        bookings = courtList3.length
    }
    if (selectedTime == "13:00") {
        let bookings = courtList4.length
    }
    if (selectedTime == "14:00") {
        let bookings = courtList5.length
    }
    if (selectedTime == "15:00") {
        let bookings = courtList6.length
    }
    if (selectedTime == "16:00") {
        let bookings = courtList7.length
    }
    if (selectedTime == "17:00") {
        let bookings = courtList8.length
    }
    if (selectedTime == "18:00") {
        let bookings = courtList9.length
    }
    if (selectedTime == "19:00") {
        let bookings = courtList10.length
    }
    if (selectedTime == "20:00") {
        let bookings = courtList11.length
    }

    let courtField = document.getElementById("id_court_number")
    courtField.value = parseInt(bookings)

    console.log("pickCourt Function Executed")
    console.log(selectedTime)
    console.log(`There are ${bookings} bookings at that time`)
}





console.log("below is the court list")
console.log(courtList)
console.log("below is the time list")
console.log(timeList)
console.log("below is the reservation count")
// courtPicker(courtList)