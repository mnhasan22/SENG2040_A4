async function fetchPosts() {
    try {
        let response = await fetch('/api/posts/');
        let posts = await response.json();
        let container = document.getElementById('posts');
        container.innerHTML = '';
        posts.forEach(post => {
            let div = document.createElement('div');
            div.innerHTML = `<h2>${post.title}</h2><p>${post.content}</p>`;
            container.appendChild(div);
        });
    } catch (err) {
        console.error("Failed to fetch posts:", err);
    }
}

document.addEventListener('DOMContentLoaded', fetchPosts);
