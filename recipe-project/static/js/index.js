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

// Get references to the HTML elements
const menuBars = document.getElementById('menu-bars'); // The hamburger menu icon
const menuClose = document.getElementById('menu-close'); // The close icon for the mobile menu
const mobileMenu = document.querySelector('.mobile-menu'); // The list of menu items in the mobile menu

// Create a variable to track the menu state
let menuOpen = false; // Variable to track whether the mobile menu is open or closed

// Add a click event listener to the hamburger menu icon
menuBars.addEventListener('click', () => {
    // Toggle the menu state by changing the value of the menuOpen variable
    menuOpen = !menuOpen; // If it was open, now it's closed, and vice versa

    if (menuOpen) {
        // When menuBars is clicked, show the mobile menu, change the icon to "X"
        mobileMenu.style.display = 'block'; // Display the mobile menu by setting its style to 'block'
        menuBars.style.display = 'none'; // Hide the menuBars icon by setting its style to 'none'
        menuClose.style.display = 'block'; // Display the menuClose icon by setting its style to 'block'
    }
});

menuClose.addEventListener('click', () => {

    // When menuClose is clicked or menuBars is clicked again, close the mobile menu, change the icon back to menuBars
    mobileMenu.style.display = 'none'; // Hide the mobile menu by setting its style to 'none'
    menuBars.style.display = 'block'; // Display the menuBars icon by setting its style to 'block'
    menuClose.style.display = 'none'; // Hide the menuClose icon by setting its style to 'none'
});



document.addEventListener("DOMContentLoaded", function () {
    const recipeItems = document.querySelectorAll(".uk-card");

    recipeItems.forEach(function (recipeItem, index) {
        const heartIcon = recipeItem.querySelector(".heart-icon a");
        const recipeData = recipeItem.querySelector(".recipe-data");

        // Add a unique identifier to the uk-card element, e.g., data-recipe-id
        recipeItem.setAttribute("data-recipe-id", index);

        // Retrieve the recipe information
        const title = recipeData.querySelector(".uk-card-title").textContent;

        // Retrieve the image source
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



// code To create a shopping list from the HTML list 
// Add an event listener to the "Generate PDF" button
document.getElementById('generate-pdf').addEventListener('click', function () {
    // Extract list items
    const listItems = document.querySelectorAll('.custom-list li');

    // an empty array to store the shopping list items
    const shoppingList = [];
    listItems.forEach(function (item) {
      shoppingList.push(item.textContent);
    });

    // Generate a shopping list as a string
    const shoppingListText = shoppingList.join('\n');

    // Create a PDF
    html2pdf().from(shoppingListText).outputPdf(function (pdf) {
      // Download the PDF
      const pdfBlob = new Blob([pdf], { type: 'application/pdf' });
      const url = URL.createObjectURL(pdfBlob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'shopping-list.pdf';
      a.click();
      URL.revokeObjectURL(url);
    });
  });