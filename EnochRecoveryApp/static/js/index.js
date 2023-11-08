var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
    // This function will display the specified tab of the form...
    var x = document.getElementsByClassName("tab");
    x[n].style.display = "block";
    //... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "Submit";
    } else {
        document.getElementById("nextBtn").innerHTML = "Next";
    }
    //... and run a function that will display the correct step indicator:
    fixStepIndicator(n);
}

function nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
        // ... the form gets submitted:
        document.getElementById("regForm").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function validateForm() {
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[currentTab].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:
    for (i = 0; i < y.length; i++) {
        // If a field is empty...
        if (y[i].value == "") {
            // add an "invalid" class to the field:
            y[i].className += " invalid";
            // and set the current valid status to false
            valid = false;
        }
    }
    // If the valid status is true, mark the step as finished and valid:
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid; // return the valid status
}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}

// Modify the function to populate time slots based on the schedule
function setDefaultDateTime() {
    var dateInput = document.getElementById("id_date");
    var timeSelect = document.getElementById("id_time");

    // Check if a date is selected
    if (dateInput.value) {
        var selectedDate = new Date(dateInput.value);
        var selectedDayOfWeek = selectedDate.getDay();

        var timeSlots = {
            0: ["5:30 PM", "6:00 PM", "6:30 PM"],
            1: ["5:30 PM", "6:00 PM", "6:30 PM"],
            2: ["5:30 PM", "6:00 PM", "6:30 PM"],
            5: ["10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM"],
            6: ["2:30 PM", "3:00 PM", "3:30 PM"],
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

    // Compare the selected date with the current date
    if (selectedDate < today) {
        if (selectedDate.toDateString() !== today.toDateString()) {
            alert("Please select a date in the future.");
            dateInput.value = ""; // Clear the date input
        }
    }
}

var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 5000); // Change slides every 5 seconds
}

function plusDivs(n) {
    slideIndex += n;
    var slides = document.getElementsByClassName("mySlides");
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    if (slideIndex < 1) {
        slideIndex = slides.length;
    }
    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";
}

// Call the function to set the default date when the page is loaded
setDefaultDate();

// Call the function to populate time slots based on the selected date
setDefaultDateTime();

// Add an event listener to the date input to update time options when the date changes
document.getElementById("id_date").addEventListener("change", setDefaultDateTime);


// Add an event listener to the date input to validate the date
document.getElementById("id_date").addEventListener("change", validateDate);

var shortText = document.getElementById('short-text');
var fullText = document.getElementById('full-text');
var msg = document.getElementById('msg');
var readMoreLink = document.getElementById('read-more-link');
var isExpanded = false;

function toggleText() {
    if (isExpanded) {
        shortText.style.display = 'block';
        msg.style.display = 'block'; // Show the "Message From Our Director" text
        fullText.style.display = 'none';
        readMoreLink.innerText = 'Read More';
        isExpanded = false;
    } else {
        shortText.style.display = 'none';
        fullText.style.display = 'block';
        readMoreLink.innerText = 'Read Less';
        msg.style.display = 'none'; // Hide the "Message From Our Director" text
        isExpanded = true;
    }
}

var videoContainer = document.getElementById('video-container');
var iframe = videoContainer.querySelector('iframe');

// Listen for a click event to expand the video
videoContainer.addEventListener('click', function () {
    if (iframe.src === '') {
        // Load the video when clicked for the first time
        iframe.src = 'https://drive.google.com/file/d/1A-pwWvWQlDmdfSzftqMuhB8KWUnu_rgk/preview';
    }

    // Expand the video to full size
    videoContainer.style.width = '100%';
});
