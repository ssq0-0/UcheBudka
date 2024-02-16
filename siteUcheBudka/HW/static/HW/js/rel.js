document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Предотвращаем стандартную отправку формы

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const csrftoken = document.querySelector('input[name=csrfmiddlewaretoken]').value;

    fetch('/api/v1/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({username: username, password: password})
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Если авторизация успешна, читаем токены
        } else {
            throw new Error('Авторизация не удалась'); // Иначе генерируем ошибку
        }
    })

    .then(data => {
    // Сохраняем токены в localStorage
    localStorage.setItem('access_token', data.access);
    localStorage.setItem('refresh_token', data.refresh);
    // Изменяем URL в адресной строке без перезагрузки страницы
//    console.log(token);
    window.location.href = '/api/v1/main/';
    });
//    .catch(error => {
//        console.error('Ошибка:', error);
//    });
});

