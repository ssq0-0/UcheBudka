document.addEventListener('DOMContentLoaded', function (){
    const token = localStorage.getItem('access_token');
//    const csrftoken = document.querySelector('meta[name=csrfmiddlewaretoken]').getAttribute('content');

    if(!token){
        console.log('Нет токена');
    }else {
        fetch('/api/v1/main/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
//                'X-CSRFToken': csrftoken
            }
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else if (response.status === 401) {
                    // Токен может быть истекшим, можно попытаться обновить его с помощью refresh token
                    throw new Error('Необходима повторная авторизация');
                } else {
                    throw new Error('Ошибка доступа к защищенному ресурсу');
                }
            })
            .then(data => {
                // Обработка данных, полученных от API
                console.log(data);
            })
    }
    fetch('/api/v1/mainHW/', {
       method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
           }
    })
    .then(response => {
    if (!response.ok) {
        throw new Error('Ошибка при получении уведомлений');
    }
    return response.json();
})
.then(data => {
    const notificationsSection = document.getElementById('sctnew').querySelector('div');

    data.forEach(notification => {
        const notificationElement = document.createElement('div'); // Можно заменить на другой тег, если нужно
        notificationElement.innerHTML = `
            <p>Предмет: ${notification.school_subject}</p>

        `;
        notificationsSection.appendChild(notificationElement);
    });
})
.catch(error => {
    console.error('Ошибка:', error);
});
});
