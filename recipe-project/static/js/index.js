// When the DOM is fully loaded, execute the following code
document.addEventListener('DOMContentLoaded', function () {

    // Get all elements with the 'expandable' class
    const expandableList = document.querySelectorAll('.expandable');

    // Iterate through each 'expandable' element
    expandableList.forEach(item => {
        const icon = item.querySelector('.icon'); // Get the icon within the 'expandable' element
        const subList = item.querySelector('.sublist'); // Get the sublist within the 'expandable' element

        // Add a click event listener to the icon
        icon.addEventListener('click', function () {
            if (subList.style.display === 'none' || subList.style.display === '') {
                icon.textContent = '-'; // Change the icon to '-' if the sublist is hidden
                subList.style.display = 'block'; // Display the sublist
            }
            else {
                icon.textContent = ('+'); // Change the icon to '+' if the sublist is visible
                subList.style.display = 'none'; // Hide the sublist
            }
        });

        // Close the sublists on page reload
        if (subList.style.display === 'none' || subList.style.display === '') {
            icon.textContent = '+';
        }
    });
});

// Add a click event listener to step icons to fade associated step content
const icons = document.querySelectorAll('.step-icon');

icons.forEach(icon => {
    icon.addEventListener('click', function () {
        const stepContent = this.nextElementSibling; // Get the associated step content
        stepContent.classList.add('fade-lower'); // Add a class to adjust the position with CSS for fading
    });
});

// Get references to menu-related HTML elements
const menuBars = document.getElementById('menu-bars'); // The hamburger menu icon
const menuClose = document.getElementById('menu-close'); // The close icon for the mobile menu
const mobileMenu = document.querySelector('.mobile-menu'); // The list of menu items in the mobile menu

// Create a variable to track the mobile menu state
let menuOpen = false; // Variable to track whether the mobile menu is open or closed

// Add a click event listener to the hamburger menu icon
menuBars.addEventListener('click', () => {
    menuOpen = !menuOpen; // Toggle the menu state (open or closed)

    if (menuOpen) {
        mobileMenu.style.display = 'block'; // Show the mobile menu
        menuBars.style.display = 'none'; // Hide the hamburger menu icon
        menuClose.style.display = 'block'; // Show the close icon for the mobile menu
    }
});

// Add a click event listener to the close icon for the mobile menu
menuClose.addEventListener('click', () => {
    mobileMenu.style.display = 'none'; // Hide the mobile menu
    menuBars.style.display = 'block'; // Show the hamburger menu icon
    menuClose.style.display = 'none'; // Hide the close icon for the mobile menu
});

// When the DOM is fully loaded, execute the following code
document.addEventListener("DOMContentLoaded", function () {
    // Get all elements with the class 'uk-card' (likely recipe items)
    const recipeItems = document.querySelectorAll(".uk-card");

    // Iterate through each 'uk-card' element
    recipeItems.forEach(function (recipeItem, index) {
        const heartIcon = recipeItem.querySelector(".heart-icon a"); // Find the heart icon
        const recipeData = recipeItem.querySelector(".recipe-data"); // Find recipe data

        // Add a unique identifier to the 'uk-card' element
        recipeItem.setAttribute("data-recipe-id", index);

        // Retrieve the recipe title from the recipe data
        const title = recipeData.querySelector(".uk-card-title").textContent;

        // Retrieve the image source for the recipe
        const imageSrc = recipeItem.querySelector("img").getAttribute("src");

        // Create an object to store the recipe data
        const recipe = {
            id: recipeItem.getAttribute("data-recipe-id"),
            title: title,
            imageSrc: imageSrc, // Add the image source to the object
        };

        // Check if the recipe is already in local storage
        const existingRecipe = localStorage.getItem(`recipe-${recipe.id}`);

        if (existingRecipe) {
            // Change the heart icon color to red for existing favorite recipes
            heartIcon.querySelector("svg path").setAttribute("fill", "red");
        }

        // Add a click event listener to the heart icon
        heartIcon.addEventListener("click", function (event) {
            event.preventDefault();

            if (existingRecipe) {
                alert("Recipe is already in favorites!");
            } else {
                // Change the heart icon color to red
                heartIcon.querySelector("svg path").setAttribute("fill", "red");

                // Add the recipe to local storage 
                localStorage.setItem(`recipe-${recipe.id}`, JSON.stringify(recipe));

                // Display a confirmation message
                alert("Recipe added to favorites!");
            }
        });
    });
});
