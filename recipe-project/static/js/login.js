// Get references to error message elements
const emailError = document.getElementById('email-error'); // Element for email validation error messages
const submitError = document.getElementById('submit-error'); // Element for general submission error messages
const passwordError = document.getElementById('password-error'); // Element for password validation error messages

// Function to validate an email address
function validateEmail () {
  const email = document.getElementById('email').value; // Get the email input value

  // Check if the email is empty
  if (email.length === 0) {
    emailError.innerText = 'Enter an Email Address'; // Display an error message for an empty email
    emailError.style.color = 'red'; // Set the error message color to red
    return false; // Return false to indicate validation failure
  }

  // Check if the email matches a valid format using a regular expression
  if (!email.match(/^[a-zA-Z\]\._\-[0-9]*[@][a-zA-Z]*[\.][a-z]{2,}$/)) {
    emailError.innerText = 'Enter valid email address'; // Display an error message for an invalid email format
    emailError.style.color = 'red'; // Set the error message color to red
    return false; // Return false to indicate validation failure
  }

  emailError.innerText = 'Valid'; // Display a "Valid" message if the email is valid
  emailError.style.color = 'green'; // Set the success message color to green
  return true; // Return true to indicate successful validation
}

// Function to validate the password
function validatePassword () {
  const password = document.getElementById('password').value; // Get the password input value

  // Regular expressions for password validation
  const lengthRegex = /.{8,}/; // The password must be at least eight characters long
  const uppercaseRegex = /[A-Z]/; // The password must contain at least one uppercase character
  const lowercaseRegex = /[a-z]/; // The password must contain at least one lowercase character
  const digitRegex = /\d+/; // The password must contain at least one numeric digit
  const specialCharRegex = /[!@#$%^&*]/; // The password must contain at least one special character (e.g., !@#$%^&*)

  // Check each password validation criteria using regular expressions
  if (!uppercaseRegex.test(password)) {
    passwordError.innerHTML = 'The password must contain at least one uppercase letter.'; // Display an error message
    passwordError.style.color = 'red'; // Set the error message color to red
    return false; // Return false to indicate validation failure
  }
  if (!lowercaseRegex.test(password)) {
    passwordError.innerHTML = 'The password must contain at least one lowercase letter.'; // Display an error message
    passwordError.style.color = 'red'; // Set the error message color to red
    return false; // Return false to indicate validation failure
  }
  if (!digitRegex.test(password)) {
    passwordError.textContent = 'The password must contain at least one numeric digit'; // Display an error message
    passwordError.style.color = 'red'; // Set the error message color to red
    return false; // Return false to indicate validation failure
  }
  if (!specialCharRegex.test(password)) {
    passwordError.textContent = 'The password must contain at least one special character (e.g., !@#$%^&*)'; // Display an error message
    passwordError.style.color = 'red'; // Set the error message color to red
    return false; // Return false to indicate validation failure
  }
  if (!lengthRegex.test(password)) {
    passwordError.innerHTML = 'The password must be at least 8 characters long.'; // Display an error message
    passwordError.style.color = 'red'; // Set the error message color to red
    return false; // Return false to indicate validation failure
  }

  passwordError.innerHTML = 'valid'; // Display a "Valid" message if the password is valid
  passwordError.style.color = 'green'; // Set the success message color to green
  return true; // Return true to indicate successful validation
}
