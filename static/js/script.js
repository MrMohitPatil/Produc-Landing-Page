// Get all elements with class 'faq'
var faqElements = document.querySelectorAll('.faq');

// Loop through each 'faq' element and add a click event listener
faqElements.forEach(function(faqElement) {
    faqElement.addEventListener('click', function() {
        // Toggle the 'faq-content' visibility
        var faqContent = this.querySelector('.faq-content');
        if (faqContent.style.display === 'none' || faqContent.style.display === '') {
            faqContent.style.display = 'block';
        } else {
            faqContent.style.display = 'none';
        }
    });
});
