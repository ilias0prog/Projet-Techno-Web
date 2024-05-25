

    // Exemple d'utilisation : appeler cette fonction lorsque l'utilisateur appuie sur un bouton
    async function handleLoadCommentsButtonClick(articleId) {
        const comments = await loadComments(articleId);
        // Utilisez les commentaires récupérés pour mettre à jour l'interface utilisateur
        console.log('Comments:', comments);
}

document.getElementById('search-toggle').addEventListener('click', function(event) {
    event.preventDefault();
    var searchMenu = document.getElementById('search-menu');
    if (searchMenu.style.display === 'none' || searchMenu.style.display === '') {
        searchMenu.style.display = 'block';
    } else {
        searchMenu.style.display = 'none';
    }
});

function toggleSearchOption(option) {
    var searchTheme = document.getElementById('search-theme');
    var searchDate = document.getElementById('search-date');
    if (option === 'theme') {
        searchTheme.style.display = 'block';
        searchDate.style.display = 'none';
    } else if (option === 'date') {
        searchTheme.style.display = 'none';
        searchDate.style.display = 'block';
    }
}

document.addEventListener('click', function(event) {
    var searchMenu = document.getElementById('search-menu');
    var searchToggle = document.getElementById('search-toggle');
    if (!searchMenu.contains(event.target) && !searchToggle.contains(event.target)) {
        searchMenu.style.display = 'none';
    }
});


// Search menu part :


function toggleSearchOption(option) {
    document.getElementById('search-theme').style.display = option === 'theme' ? 'block' : 'none';
    document.getElementById('search-date').style.display = option === 'date' ? 'block' : 'none';
}

function performSearch() {
    const selectedOption = document.querySelector('input[name="search-option"]:checked').value;
    if (selectedOption === 'theme') {
        const theme = document.getElementById('search-article-theme').value;
        if (theme) {
            window.location.href = `/articles/homepage/search_theme/${theme}`;
        } else {
            alert('Please select a theme.');
        }
    } else if (selectedOption === 'date') {
        const date = document.getElementById('search-article-date').value;
        if (date) {
            window.location.href = `/articles/homepage/search_date/${date}`;
        } else {
            alert('Please select a date.');
        }
    } else {
        alert('Please select a search option.');
    }
}


// Confirm delete message :
function confirmDelete(event, articleId) {
    event.preventDefault();
    if (confirm('Are you sure you want to delete this article?')) {
        document.getElementById('delete-form-' + articleId).submit();
    }
}

