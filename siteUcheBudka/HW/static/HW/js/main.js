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
