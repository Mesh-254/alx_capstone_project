
let nameError = document.getElementById("name-error");
let phoneError = document.getElementById("phone-error");

let emailError = document.getElementById("email-error");

let messageError = document.getElementById("message-error");

let submitError = document.getElementById("submit-error");


function validateName() {
    let name = document.getElementById('contact-name').value;

    if (name.length == 0) {
        nameError.innerHTML = "Please enter your Name";
    }
    if (!name.match(/^[A-Za-z]*\s{1}[A-Za-z]*$/)) {
        nameError.innerHTML = "write full name"
        return false;
    }
    nameError.innerHTML = '<i class="fa fa-check-circle-o" aria-hidden="false">'
}

function validatePhone() {
    let phone = document.getElementById("contact-phone").value;

    if (phone.length == 0) {
        phoneError.innerHTML = 'Enter a valid Phone Number';
        return false;
    }
    if (!phone.match(/^[0-9]{10}$/)) {
        phoneError.innerHTML = "use digits only/phone length";
        return false;

    }
    phoneError.innerHTML = '<i class="fa fa-check-circle-o" aria-hidden="false">'
    return true
}

function validateEmail() {
    let email = document.getElementById('contact-email').value;
    if (email.length === 0) {
        emailError.innerHTML = "Enter an Email Address";
        return false;

    }
    if (!email.match(/^[a-zA-Z\]\._\-[0-9]*[@][a-zA-Z]*[\.][a-z]{2,}$/)){
        emailError.innerHTML = "Enter valid email address";
        return false;
    }
    emailError.innerHTML = '<i class="fa fa-check-circle-o" aria-hidden="true">'
    return true
}

function validateMessage(){
    let message  = document.getElementById('message').value;
    const requiredCharacters = 50;
    const remainingCharacters = requiredCharacters-message.length;
    if(remainingCharacters > 0){
        messageError.innerHTML = remainingCharacters + "more characters required";
        return false;
    }
    messageError.innerHTML= '<i class="fa fa-check-circle-o" aria-hidden="true">';
    return true;
}
