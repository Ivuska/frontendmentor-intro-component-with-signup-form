let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes);
const firstname = id("firstname"),
  lastname = id("lastname"),
  email = id("email"),
  password = id("password"),
  form = id("form"),
  errorMsg = classes("error"),
  successIcon = classes("success-icon"),
  failureIcon = classes("failure-icon");

function MarkAsInvalid(id, serial, message) {
  errorMsg[serial].innerHTML = message;
  id.classList.remove("valid");
  id.classList.add("invalid");

  failureIcon[serial].style.opacity = "1";
  successIcon[serial].style.opacity = "0";
  return false;
}

//real function
function MarkAsValid(id, serial) {
  errorMsg[serial].innerHTML = "";
  id.classList.add("valid");
  id.classList.remove("invalid");

  failureIcon[serial].style.opacity = "0";
  successIcon[serial].style.opacity = "1";
  return true;
}

//in the variable 'engine' is an anonymous function with three parameters smth like lambda in Python
const engine = (id, serial, message) => {
  if (id !== email) {
    if (id.value.trim() === "") {
      return MarkAsInvalid(id, serial, message);
    } else {
      return MarkAsValid(id, serial);
    }
  } else {
    if (id.value.trim().includes("@")) {
      return MarkAsValid(id, serial);
    } else {
      return MarkAsInvalid(id, serial, message);
    }
  }
};

function SubmitAndSendForm() {
  alert(
    "Your form has been submitted. \nPlease check your email for address verification."
  );
  form.reset();
  const inputs = document.querySelectorAll(
    "#firstname, #lastname, #email, #password"
  );
  const serials = [0, 1, 2, 3];

  inputs.forEach((input) => {
    input.classList.remove("valid");
  });
  serials.forEach((serial) => {
    successIcon[serial].style.opacity = "0";
  });
}

function ValidateInputFields(element) {
  element.preventDefault();
  const firstname_ok = engine(firstname, 0, "Firstname cannot be empty.");
  const lastname_ok = engine(lastname, 1, "Lastname cannot be empty.");
  const email_ok = engine(email, 2, "Looks like this is not a valid email address.");
  const password_ok = engine(password, 3, "Password cannot be empty.");

  if (firstname_ok && lastname_ok && email_ok && password_ok === true) {
    SubmitAndSendForm();
  } else {
    //prevents sending the form
  
  }
}

//Check if the field is filled when input lost focus.
//More info to blur event https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event
firstname.addEventListener("blur", () => {
  engine(firstname, 0, "Firstname cannot be empty.");
});

lastname.addEventListener("blur", () => {
  engine(lastname, 1, "Lastname cannot be empty.");
});

email.addEventListener("blur", () => {
  engine(email, 2, "Looks like this is not a valid email address.");
});

password.addEventListener("blur", () => {
  engine(password, 3, "Password cannot be empty.");
});

//Check the inputs when the form is submitted.
form.addEventListener("submit", ValidateInputFields);
