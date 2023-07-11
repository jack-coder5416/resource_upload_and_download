
document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('upload-form');
    var titleInput = document.getElementById('title');
    var fileInput = document.getElementById('file');

    form.addEventListener('submit', function(event) {
        var title = titleInput.value.trim();
        var file = fileInput.value;

        if (title === '' || file === '') {
            event.preventDefault();
            displayErrorMessage('Please fill in all fields.');
        }
    });

    function displayErrorMessage(message) {
        var errorContainer = document.getElementById('error-message-container');
        var errorMessage = document.getElementById('error-message');

        errorMessage.textContent = message;
        errorContainer.style.display = 'block';
    }
});
