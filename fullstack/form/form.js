document.getElementById("registrationForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const name = document.getElementById("name");
  const email = document.getElementById("email");
  const phone = document.getElementById("phone");
  const dob = document.getElementById("dob");
  const terms = document.getElementById("terms");
  const course = document.getElementById("course");
  const confirmation = document.getElementById("confirmation");

  let valid = true;

  // Name validation
  if (!/^[a-zA-Z\s]+$/.test(name.value)) {
    document.getElementById("nameError").innerText = "Name should contain letters and spaces only";
    valid = false;
  } else {
    document.getElementById("nameError").innerText = "";
  }

  // Email validation
  if (!/^\S+@\S+\.\S+$/.test(email.value)) {
    document.getElementById("emailError").innerText = "Enter a valid email";
    valid = false;
  } else {
    document.getElementById("emailError").innerText = "";
  }

  // Phone validation
  if (!/^\d{10}$/.test(phone.value)) {
    document.getElementById("phoneError").innerText = "Enter a valid 10-digit phone number";
    valid = false;
  } else {
    document.getElementById("phoneError").innerText = "";
  }

  // DOB validation
  const inputDate = new Date(dob.value);
  const today = new Date();
  if (inputDate > today) {
    document.getElementById("dobError").innerText = "Date of Birth cannot be in the future";
    valid = false;
  } else {
    document.getElementById("dobError").innerText = "";
  }

  // Terms & Conditions
  if (!terms.checked) {
    document.getElementById("termsError").innerText = "You must accept the terms";
    valid = false;
  } else {
    document.getElementById("termsError").innerText = "";
  }

  if (valid) {
    confirmation.innerText = `🎉 Thank you ${name.value}! You have registered for ${course.value}.`;
    confirmation.style.display = "block";
    this.reset();
  }
});
