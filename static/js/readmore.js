document.addEventListener('DOMContentLoaded', function () {
    var shortText = document.getElementById('short-text');
    var fullText = document.getElementById('full-text');
    var img = document.getElementById('img');
    var msg = document.getElementById('msg');
    var readMoreLink = document.getElementById('read-more-link');
    var isExpanded = false;

    function toggleText() {
        isExpanded = !isExpanded; // Toggle the value

        shortText.style.display = isExpanded ? 'none' : 'block';
        fullText.style.display = isExpanded ? 'block' : 'none';
        img.style.display = isExpanded ? 'block' : 'none';
        msg.style.display = isExpanded ? 'none' : 'block';

        readMoreLink.innerText = isExpanded ? 'Read Less' : 'Read More';
    }

    // Add a click event listener to the "Read More" link
    readMoreLink.addEventListener('click', toggleText);
});
