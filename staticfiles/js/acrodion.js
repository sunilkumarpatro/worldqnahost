var accordions = document.querySelectorAll('.accordion-item');

  accordions.forEach(function(acc) {
    acc.addEventListener('click', function() {
      if (!this.classList.contains('active')) {
        accordions.forEach(function(item) {
          item.classList.remove('active');
        });
        this.classList.add('active');
      } else {
        this.classList.remove('active');
      }
    });
  });
  document.addEventListener('DOMContentLoaded', function() {
    const commentsContainer = document.querySelector('.comments-section');
    const loadMoreBtn = document.getElementById('load-more-btn');

    const comments = Array.from(document.querySelectorAll('.comment'));
    const initialCommentsToShow = 10;
    let visibleComments = initialCommentsToShow;

    // Function to toggle visibility of comments
    function toggleCommentsVisibility() {
        comments.forEach((comment, index) => {
            comment.style.display = index < visibleComments ? 'block' : 'none';
        });
    }

    // Initially show only the first 'initialCommentsToShow' comments
    toggleCommentsVisibility();

    // Show more comments when the 'Load More' button is clicked
    loadMoreBtn.addEventListener('click', function() {
        visibleComments += initialCommentsToShow;
        toggleCommentsVisibility();

        // Hide the 'Load More' button if all comments are visible
        if (visibleComments >= comments.length) {
            loadMoreBtn.style.display = 'none';
        }
    });
});
