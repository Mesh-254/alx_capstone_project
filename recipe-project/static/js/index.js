document.addEventListener('DOMContentLoaded', function () {
    
    const expandableList = document.querySelectorAll('.expandable');
    expandableList.forEach(item => {
        const icon = item.querySelector('.icon');
        const subList = item.querySelector('.sublist');
        icon.addEventListener('click', function () {
            if (subList.style.display === 'none' || subList.style.display === '') {
                icon.textContent = '-'
                subList.style.display = 'block';
            }
            else {
                icon.textContent = ('+');
                subList.style.display = 'none';
            }
        });
        // close the sublists on page reload
        if (subList.style.display === 'none' || subList.style.display === '') {
            icon.textContent = '+';
        }
    })
});


// Fade text in detail page when step icon is clicked 
// Get all step-icon elements
const icons = document.querySelectorAll('.step-icon');

// Add a click event listener to each step-icon
icons.forEach(icon => {
    icon.addEventListener('click', function () {
        // Get the associated step-content element
        const stepContent = this.nextElementSibling;
        // Add a class to adjust the position with CSS
        stepContent.classList.add('fade-lower');
    });
});




