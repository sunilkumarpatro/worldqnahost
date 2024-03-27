document.getElementById("myForm").addEventListener("submit", function(event) {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;
    var successMessage = document.querySelector('.success');
    var nameError = document.getElementById('nameLengthError');
    var emailError = document.getElementById('emailLengthError');
    var messageError = document.getElementById('messageLengthError');
    var generalError = document.querySelector('.error');

    // Reset error messages
    nameError.style.display = "none";
    emailError.style.display = "none";
    messageError.style.display = "none";
    generalError.style.display = "none";

    var valid = true; // Flag to track form validity

    if (name.length < 5) {
        nameError.style.display = "block";
        valid = false; // Set flag to false if content is invalid
    }

    if (email.length < 10) {
        emailError.style.display = "block";
        valid = false; // Set flag to false if content is invalid
    }

    if (message.length < 15) {
        messageError.style.display = "block";
        valid = false; // Set flag to false if content is invalid
    }

    if (!valid) {
        event.preventDefault(); // Prevent form submission if any field is invalid
        successMessage.style.display = 'none'; // Hide success message if there are errors
    } else {
        // Show success message
        successMessage.style.display = 'block';

        // Countdown timer
        var countdownElement = document.getElementById('successCountdown');
        var countdown = 10;
        var countdownInterval = setInterval(function() {
            countdown--;
            countdownElement.textContent = countdown;
            if (countdown <= 0) {
                clearInterval(countdownInterval);
                // Submit form after 2 seconds of showing success message
                setTimeout(function() {
                    document.getElementById("myForm").submit();
                }, 2000);
            }
        }, 1000);

        event.preventDefault(); // Prevent form submission
    }
});