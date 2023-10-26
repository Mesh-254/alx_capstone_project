// Get references to error message elements
let emailError = document.getElementById("email-error"); // Element for email validation error messages
let submitError = document.getElementById("submit-error"); // Element for general submission error messages
let passwordError = document.getElementById('password-error'); // Element for password validation error messages
let nameError = document.getElementById('name-error'); // Element for name validation error messages

// Function to validate the user's name
function validateName() {
    let name = document.getElementById('name').value; // Get the name input value

    // Check if the name is empty
    if (name.length == 0) {
        nameError.textContent = "Please enter your Name"; // Display an error message for an empty name
        return false; // Return false to indicate validation failure
    }

    // Check if the name matches a valid format using a regular expression
    if (!name.match(/^[A-Za-z]+\s[A-Za-z]+(\s[A-Za-z]+)?$/)) {
        nameError.textContent = "Write full name"; // Display an error message for an invalid name format
        nameError.style.color = "red"; // Set the error message color to red
        return false; // Return false to indicate validation failure
    }

    nameError.innerHTML = 'Valid'; // Display a "Valid" message if the name is valid
    nameError.style.color = "green"; // Set the success message color to green
}

// Function to validate the email address
function validateEmail() {
    let email = document.getElementById('email').value; // Get the email input value

    // Check if the email is empty
    if (email.length === 0) {
        emailError.innerText = "Enter an Email Address"; // Display an error message for an empty email
        return false; // Return false to indicate validation failure
    }

    // Check if the email matches a valid format using a regular expression
    if (!email.match(/^[a-zA-Z\]\._\-[0-9]*[@][a-zA-Z]*[\.][a-z]{2,}$/)) {
        emailError.innerText = "Enter a valid email address"; // Display an error message for an invalid email format
        emailError.style.color = "red"; // Set the error message color to red
        return false; // Return false to indicate validation failure
    }

    emailError.innerText = 'Valid'; // Display a "Valid" message if the email is valid
    emailError.style.color = "green"; // Set the success message color to green
    return true; // Return true to indicate successful validation
}

// Function to validate the password
function validatePassword() {
    const password = document.getElementById("password").value; // Get the password input value

    // Regular expressions for password validation
    const lengthRegex = /.{8,}/; // The password must be at least eight characters long
    const uppercaseRegex = /[A-Z]/; // The password must contain at least one uppercase character
    const lowercaseRegex = /[a-z]/; // The password must contain at least one lowercase character
    const digitRegex = /\d+/; // The password must contain at least one numeric digit
    const specialCharRegex = /[!@#$%^&*]/; // The password must contain at least one special character (e.g., !@#$%^&*)

    // Check each password validation criteria using regular expressions
    if (!uppercaseRegex.test(password)) {
        passwordError.innerHTML = "The password must contain at least one uppercase letter."; // Display an error message
        passwordError.style.color = 'red'; // Set the error message color to red
        return false; // Return false to indicate validation failure
    }
    if (!lowercaseRegex.test(password)) {
        passwordError.innerHTML = "The password must contain at least one lowercase letter."; // Display an error message
        passwordError.style.color = 'red'; // Set the error message color to red
        return false; // Return false to indicate validation failure
    }

    // Check if the password contains at least one numeric digit.
    if (!digitRegex.test(password)) {
        passwordError.textContent = "The password must contain at least one numeric digit"; // Display an error message
        return false; // Return false to indicate validation failure
    }

    if (!specialCharRegex.test(password)) {
        passwordError.textContent = "The password must contain at least one special character (e.g., !@#$%^&*)"; // Display an error message
        passwordError.style.color = 'red'; // Set the error message color to red
        return false; // Return false to indicate validation failure
    }
    
    if (!lengthRegex.test(password)) {
        passwordError.innerHTML = "The password must be at least 8 characters long."; // Display an error message
        passwordError.style.color = 'red'; // Set the error message color to red
        return false; // Return false to indicate validation failure
    }

    passwordError.innerHTML = 'Valid'; // Display a "Valid" message if the password is valid
    passwordError.style.color = 'green'; // Set the success message color to green
    return true; // Return true to indicate successful validation
}

// Function to confirm the password
function confirmPassword() {
    const password = document.getElementById("password").value; // Get the password input value
    const confirmPassword = document.getElementById("confirm-password").value; // Get the confirm password input value
    const confirmError = document.getElementById("confirm-password-error"); // Element for confirm password validation messages

    if (password === confirmPassword) {
        confirmError.textContent = "Passwords matched"; // Display a message for matching passwords
        confirmError.style.color = "green"; // Set the success message color to green
    } else {
        confirmError.textContent = "Passwords do not match"; // Display an error message for non-matching passwords
        confirmError.style.color = "red"; // Set the error message color to red
    }
}
