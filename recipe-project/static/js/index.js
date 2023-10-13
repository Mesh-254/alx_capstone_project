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
const icon = document.getElementsByClassName('step');
function fadeText() {
    const para = document.getElementsByClassName('step-content');
    icon.addEventListener('click', function(){
        console.log('you clicked me')
        para.style.opacity  = 0.2;
    })
}