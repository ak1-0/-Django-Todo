function deleteTodo(todoId) {
    if (confirm('Вы уверены, что хотите удалить эту задачу?')) {
        fetch(`/tasks/${todoId}/delete/`, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),  // Обязательно добавьте CSRF-токен для защиты
            },
        })
        .then(response => {
            if (response.ok) {
                location.reload();  // Перезагрузите страницу после удаления
            } else {
                alert('Ошибка при удалении задачи.');
            }
        });
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}