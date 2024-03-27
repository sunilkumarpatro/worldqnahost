var countdownTimer;
var countdownRunning = false;
var formSubmitted = false;

// Function to update hidden input with editor content
function updateHiddenInput() {
    var editorContent = document.getElementById('editor').innerText;
    document.getElementById('englishTitleQuestion').value = editorContent.trim();
}

// Function to handle image upload
function handleImageUpload(input) {
    var editor = document.getElementById('editor');
    var errorMessage = document.getElementById('errorMessage');
    var uploadButton = document.getElementById('uploadButton');
    var imageLengthError = document.getElementById('imageLengthError');

    if (input.files && input.files[0]) {
        if (input.files[0].size > 6 * 1024 * 1024) { // Check if file size is greater than 2MB
            imageLengthError.style.display = 'block'; // Display image length error message
            return; // Exit function
        } else {
            imageLengthError.style.display = 'none'; // Hide image length error message if size is within limit
        }

        var reader = new FileReader();

        reader.onload = function (e) {
            var textContent = editor.textContent || editor.innerText;

            var img = document.createElement('img');
            img.src = e.target.result;
            img.alt = 'Uploaded Image';
            img.style.width = '100%';

            editor.textContent = textContent;

            editor.appendChild(document.createElement('br'));
            editor.appendChild(img);

            errorMessage.innerHTML = '';
            updateHiddenInput();

            // Change button text to "Remove Image"
            uploadButton.innerText = 'Remove Image';
            uploadButton.onclick = removeImage; // Set the click event to removeImage
        };

        reader.readAsDataURL(input.files[0]);
    } else {
        errorMessage.innerHTML = 'Error uploading image.';
    }
}

// Function to remove uploaded image
function removeImage() {
    var editor = document.getElementById('editor');
    var uploadButton = document.getElementById('uploadButton');
    var imageUploader = document.getElementById('imageUploader');
    var images = editor.getElementsByTagName('img');

    if (images.length > 0) {
        editor.removeChild(images[0]); // Remove the first image
        uploadButton.innerText = 'Upload Image'; // Change button text back to "Upload Image"
        uploadButton.onclick = function () {
            imageUploader.click();
        }; // Set the click event to trigger file input click
        updateHiddenInput(); // Update the hidden input value after removing the image

        // Reset input file to remove the uploaded image
        imageUploader.value = ''; // Reset the input file element value
    }
}

// Function to submit form
function submitForm() {
    // Check if the form has already been submitted
    if (formSubmitted) {
        alert("Form already submitted. Please wait for the response.");
        return false; // Prevent further form submissions
    }

    // Retrieve the form content
    var textContent = document.getElementById('editor').textContent || document.getElementById('editor').innerText;

    // Validate the form content
    if (textContent.length < 10) {
        document.getElementById('nameLengthError').style.display = 'block';
        return false; // Prevent form submission
    } else {
        document.getElementById('nameLengthError').style.display = 'none'; // Hide name length error message
    }

    if (textContent.length > 500) {
        document.getElementById('messageLengthError').style.display = 'block';
        return false; // Prevent form submission
    } else {
        document.getElementById('messageLengthError').style.display = 'none'; // Hide message length error message
    }

    // Disable the submit button to prevent multiple clicks
    document.getElementById('submitButton').disabled = true;

    // Start the countdown for success message display
    startSuccessCountdown();

    // Set a delay before form submission (e.g., 10 seconds)
    setTimeout(function() {
        // Retrieve the form and its data
        var form = document.forms['yourFormName'];
        var formData = new FormData(form);

        // Perform AJAX submission
        var xhr = new XMLHttpRequest();
        xhr.open('POST', form.action, true);

        xhr.onload = function () {
            if (xhr.status !== 200) {
                // Handle errors if needed
                alert('Error submitting form.');
            } else {
                // Hide error messages
                document.getElementById('nameLengthError').style.display = 'none';
                document.getElementById('messageLengthError').style.display = 'none';
                document.getElementById('imageLengthError').style.display = 'none';

                // Clear the editor content after successful submission
                clearEditor();

                // Update the flag to indicate form submission
                formSubmitted = true;
            }

            // Enable the submit button after form submission
            document.getElementById('submitButton').disabled = false;
        };

        xhr.send(formData);

    }, 10000); // 10000 milliseconds = 10 seconds

    return false; // Prevent default form submission
}

// Function to start the success countdown
function startSuccessCountdown() {
    var successAlert = document.getElementById('successAlert');
    var successCountdown = document.getElementById('successCountdown');
    var editorContainer = document.querySelector('.editor-container');
    var countdown = 10; // Countdown duration in seconds

    successAlert.style.display = 'block';
    editorContainer.style.display = 'none'; // Hide the editor container during countdown

    function updateSuccessCountdown() {
        successCountdown.innerText = countdown;

        if (countdown === 0) {
            // After countdown, hide the success alert
            successAlert.style.display = 'none';
            // Display the completed form
            editorContainer.style.display = 'block';

            // Save editor content to localStorage
            var editorContent = document.getElementById('editor').innerText;
            localStorage.setItem('editorContent', editorContent);

            // Reload the page after 10 seconds
            setTimeout(function () {
                window.location.reload();
            }, 10000); // 10000 milliseconds = 10 seconds
        } else {
            countdown--;
            countdownTimer = setTimeout(updateSuccessCountdown, 1000);
        }
    }

    updateSuccessCountdown();
}

// Function to clear the editor content
function clearEditor() {
    var editor = document.getElementById('editor');
    editor.innerHTML = ''; // Clear the HTML content of the editor
    updateHiddenInput(); // Update the hidden input value after clearing the editor
}

// Function to handle page load
window.onload = function () {
    var storedEditorContent = localStorage.getItem('editorContent');
    if (!formSubmitted) {
        // Clear editor content if the form has not been submitted
        clearEditor();
    } else if (storedEditorContent) {
        // Load stored editor content only if the form has not been submitted
        document.getElementById('editor').innerText = storedEditorContent;
    }
}
