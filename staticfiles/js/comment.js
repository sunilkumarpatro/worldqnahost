document.getElementById('commentForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default form submission
    var commentInput = document.getElementById('comment').value.trim();

    if (commentInput.length < 3) {
        // If input length is less than 3 characters, show length error message
        document.getElementById('commentLengthError').style.display = 'block';
        document.getElementById('commentMaxLengthError').style.display = 'none'; // Hide max length error message
        return; // Stop further execution
    }

    if (commentInput.length > 500) {
        // If input length is more than 500 characters, show max length error message
        document.getElementById('commentLengthError').style.display = 'none'; // Hide length error message
        document.getElementById('commentMaxLengthError').style.display = 'block';
        return; // Stop further execution
    }

    // Hide error messages when the countdown starts
    hideErrorMessages();

    // Start the countdown
    startCountdown();

    // Hide the form during the countdown
    document.getElementById('commentForm').style.display = 'none';
});

function hideErrorMessages() {
    document.getElementById('commentLengthError').style.display = 'none';
    document.getElementById('commentMaxLengthError').style.display = 'none';
}

function startCountdown() {
    var seconds = 10;
    var successMessageElement = document.querySelector('.alert.success');
    var countdownTimerElement = document.getElementById('successCountdown');
    countdownTimerElement.textContent = seconds;
    successMessageElement.style.display = 'block';

    var countdownInterval = setInterval(function () {
        seconds--;
        countdownTimerElement.textContent = seconds;

        if (seconds <= 0) {
            clearInterval(countdownInterval);
            successMessageElement.style.display = 'none';
            document.getElementById('commentForm').style.display = 'block'; // Show the form after countdown completes
            document.getElementById('commentForm').submit();
        }
    }, 1000);
}
