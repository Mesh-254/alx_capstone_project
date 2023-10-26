// document.addEventListener("DOMContentLoaded", function () {
//     // Get the element where you want to display the liked recipes
//     const favoritesList = document.getElementsByClassName("recipe-items");

//     // Loop through all items in Local Storage
//     for (let key in localStorage) {
//         // Check if the key starts with "recipe-"
//         if (key.startsWith("recipe-")) {
//             // Parse the JSON data to get the recipe object
//             const recipe = JSON.parse(localStorage.getItem(key));

//             // Create an HTML element to display the recipe
//             const recipeElement = document.createElement("div");
//             recipeElement.innerHTML = `
//           <div class="uk-card">
//           <img src="${recipe.imageSrc}" alt="${recipe.title}" class=".card-image ">
            
//           <h2 class="uk-card-title">${recipe.title}</h2>
//           </div>`;

//             // Add the recipe element to the favorites list
//             favoritesList.appendChild(recipeElement);
//         }
//     }
// });
