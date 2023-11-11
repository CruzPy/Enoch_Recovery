function setDefaultDateTime() {
    var dateInput = document.getElementById("id_date");
    var timeSelect = document.getElementById("id_time");

    // Check if a date is selected
    if (dateInput.value) {
        var selectedDate = new Date(dateInput.value);

        // Add one day to the selected date
        selectedDate.setTime(selectedDate.getTime() + 24 * 60 * 60 * 1000);

        var selectedDayOfWeek = selectedDate.getDay();
        var timeSlots = {
            1: ["5:30 PM", "6:00 PM", "6:30 PM"],
            2: ["5:30 PM", "6:00 PM", "6:30 PM"],
            3: ["5:30 PM", "6:00 PM", "6:30 PM"],
            6: ["10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM"],
            7: ["2:30 PM", "3:00 PM", "3:30 PM"],
        };

        // Remove existing time options
        timeSelect.innerHTML = "";

        // Add the available time slots for the selected day
        if (timeSlots[selectedDayOfWeek]) {
            timeSlots[selectedDayOfWeek].forEach(function (time) {
                var option = document.createElement("option");
                option.value = time;
                option.textContent = time;
                timeSelect.appendChild(option);
            });
        }
    } else {
        // If no date is selected, clear the time options
        timeSelect.innerHTML = "";
    }
}


// Modify the function to set the default date to today when the page is loaded
function setDefaultDate() {
    var dateInput = document.getElementById("id_date");

    var today = new Date();
    var year = today.getFullYear();
    var month = today.getMonth() + 1; // Months are 0-indexed, so add 1
    var day = today.getDate();

    // Format the date as "YYYY-MM-DD"
    var formattedDate = year + '-' + (month < 10 ? '0' : '') + month + '-' + (day < 10 ? '0' : '') + day;

    dateInput.value = formattedDate;
}

// Function to validate the date input
function validateDate() {
    var dateInput = document.getElementById("id_date");
    var today = new Date();
    var selectedDate = new Date(dateInput.value);
    selectedDate.setTime(selectedDate.getTime() + 24 * 60 * 60 * 1000); // Add one calandar date, to selected date

    // Compare the selected date with the current date
    if (selectedDate <= today) {
        if (selectedDate.toDateString() !== today.toDateString()) {
            alert("Please select a date in the future.");
            dateInput.value = ""; // Clear the date input
        }
    }
}

// Call the function to set the default date when the page is loaded
setDefaultDate();

// Call the function to populate time slots based on the selected date
setDefaultDateTime();

// Add an event listener to the date input to update time options when the date changes
document.getElementById("id_date").addEventListener("change", setDefaultDateTime);


// Add an event listener to the date input to validate the date
document.getElementById("id_date").addEventListener("change", validateDate);