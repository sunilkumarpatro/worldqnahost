// header part
document.addEventListener("DOMContentLoaded", function () {
    // Get references to the side-bar and side-box elements
    var sideBar = document.querySelector('.side-bar');
    var sideBox = document.querySelector('.side-box');
    
    // Toggle function
    function toggleSideBox() {
        sideBox.classList.toggle('open'); // Add or remove 'open' class
    }
    
    // Add click event listener to the side-bar
    sideBar.addEventListener('click', toggleSideBox);
});
document.addEventListener("DOMContentLoaded", function () {
    // Get reference to the search-bar
    var searchBar = document.querySelector('.search-bar');

    // Add click event listener to the search-bar
    searchBar.addEventListener('click', openSearchBoxPopup);
});

function openSearchBoxPopup() {
    // Show the search-box-popup
    document.getElementById('searchBoxPopup').style.display = 'flex';
}

function closeSearchBoxPopup() {
    // Hide the search-box-popup
    document.getElementById('searchBoxPopup').style.display = 'none';
}
function toggleSelect() {
    var selectElement = document.getElementById('languageSelect');
    if (selectElement.style.display === 'none' || selectElement.style.display === '') {
        selectElement.style.display = 'block';
    } else {
        selectElement.style.display = 'none';
    }
}

// Function to navigate to the selected option's URL
function filterLanguages(event) {
    const searchInput = event.target.value.toLowerCase();
    const listItems = document.querySelectorAll('#languageList li');

    listItems.forEach(item => {
        const textContent = item.textContent.toLowerCase();
        if (textContent.includes(searchInput) || searchInput === 'all') {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

// accridion
function toggleAnswer(questionId) {
    const answer = document.getElementById(questionId);
    const icon = document.querySelector(`#${questionId} .fa-caret-down`);

    if (answer.style.display === 'block') {
        answer.style.display = 'none';
        icon.classList.remove('rotate-icon');
    } else {
        answer.style.display = 'block';
        icon.classList.add('rotate-icon');
    }
}
// Form validation and submission

