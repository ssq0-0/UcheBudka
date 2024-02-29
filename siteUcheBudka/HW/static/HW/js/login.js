const signInBtn = document.querySelector('.signin-btn');
const signUpBtn = document.querySelector('.signup-btn');
const formBox = document.querySelector('.form-box');
const body = document.body;

signInBtn.addEventListener('click', function() {
    formBox.classList.remove('active');
    body.classList.remove('active');
});

signUpBtn.addEventListener('click', function() {
    formBox.classList.add('active');
    body.classList.add('active');
});

// reg_opt.js
window.showSignInForm = function() {
    formBox.classList.remove('active');
    body.classList.remove('active');
};
