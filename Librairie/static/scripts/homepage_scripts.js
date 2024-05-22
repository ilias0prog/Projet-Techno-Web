function toggleComments(articleId) {
    const commentsContainer = document.getElementById(`comments-container-${articleId}`);
    if (commentsContainer.style.display === "none" || commentsContainer.style.display === "") {
        commentsContainer.style.display = "block";
    } else {
        commentsContainer.style.display = "none";
    }
}

function toggleCommentForm(articleId) {
    const formContainer = document.getElementById(`comment-form-${articleId}`);
    if (formContainer.style.display === "none" || formContainer.style.display === "") {
        formContainer.style.display = "block";
    } else {
        formContainer.style.display = "none";
    }
}

async function postComment(event, articleId) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const response = await fetch('/post_comment', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const comment = await response.json();
        addCommentToDOM(articleId, comment);
        form.reset();
    } else {
        console.error('Failed to post comment');
    }
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