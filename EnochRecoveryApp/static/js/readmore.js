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