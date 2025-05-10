function toggleEye() {
    var password = document.getElementById("password");
    var eyeIcon = document.getElementById("eye-icon");

    if (password.type === "password") {
        password.type = "text";
       eyeIcon.className = "bx bxs-show"
    } else {
        password.type = "password";
        eyeIcon.className = "bx bxs-hide"
    }
}

function toggleEye2() {
    var password = document.getElementById("password2");
    var eyeIcon = document.getElementById("eye-icon2");

    if (password.type === "password") {
        password.type = "text";
        eyeIcon.className = "bx bxs-show"
    } else {
        password.type = "password";
        eyeIcon.className = "bx bxs-hide"
    }
}

