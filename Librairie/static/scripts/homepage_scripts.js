function toggleCommentForm(articleId) {
    var commentForm = document.getElementById('comment-form-' + articleId);
    if (commentForm.style.display === 'none') {
        commentForm.style.display = 'block';
        } else {
        commentForm.style.display = 'none';
        }
    }

    function toggleComments(articleId) {
        // Make an AJAX request to load the comments for the given article ID
        // You can use fetch() or XMLHttpRequest for this
        // Once you have retrieved the comments, update the display on the page

        // Example of fetch() request to load comments
        fetch(`/load_comments/${articleId}`)
        .then(response => response.json())
        .then(comments => {
            // Update the display with the loaded comments
            const commentsContainer = document.getElementById('comments-container-' + articleId);
            commentsContainer.innerHTML = '';

            comments.forEach(comment => {
            const commentElement = document.createElement('div');
            commentElement.classList.add('comment');
            commentElement.innerHTML = `
                <div class="comment-author">${comment.author}</div>
                <div class="comment-content">${comment.content}</div>
            `;
            commentsContainer.appendChild(commentElement);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

function postComment(event, articleId) {
    event.preventDefault(); // Empêche le formulaire de se soumettre normalement

    // Récupérez le contenu du commentaire à partir du formulaire
    var commentContent = document.querySelector('#comment-form-' + articleId + ' textarea').value;

    // Faites une airerequête AJAX pour poster le commentaire
    //pour celauvez utiliser fetch() ou XMLHttpRequest pour cela
    // Une fois que le commentaire est posté avec succès, mettez à jour l'affichage sur laaire page

    // Exemple de requête fetch() pour poster le commentaire
    fetch('/post_comment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            article_id: articleId,
            comment: commentContent
        })
    })
    .then(response => {
        if (response.ok) {
            // Si le commentaire est posté avec succès, chargez à nouveau les commentaires de l'article
            loadComments(articleId);
            // Effacez le contenu du champ de commentaire après l'avoir posté
            document.querySelector('#comment-form-' + articleId + ' textarea').value = '';
        } else {
            console.error('Failed to post comment');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}


function addCommentToDOM(articleId, comment) {
    const commentsContainer = document.getElementById(`comments-container-${articleId}`);
    const commentElement = document.createElement('div');
    commentElement.classList.add('comment-card');
    commentElement.innerHTML = `
        <div class="comment-infos">
            <i class='bx bx-user-circle' id="comment-profilepicture"></i>
            <h3 class="comment-username">${comment.author_username}</h3>
            <h3 class="comment-date">${comment.date}</h3>
        </div>
        <p class="comment-content">${comment.content}</p>
    `;
    commentsContainer.appendChild(commentElement);
}



        async function loadComments(articleId) {
    try {
        const response = await fetch('/articles/load_comments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ article_id: articleId })
        });
        const data = await response.json();
        return data.comments;
    } catch (error) {
        console.error('Error loading comments:', error);
    }
}

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

