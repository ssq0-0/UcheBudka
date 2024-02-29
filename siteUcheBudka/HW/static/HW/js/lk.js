document.addEventListener('DOMContentLoaded', function() {
    // Функция для загрузки данных профиля
    function loadProfile() {
        const token = localStorage.getItem('access_token'); // Получаем токен из localStorage
        fetch('/api/v1/profile/', { // Используйте актуальный URL вашего API
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`, // Добавляем токен в заголовки запроса
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при получении данных');
            }
            return response.json(); // Парсим ответ в формате JSON
        })
        .then(data => {
            // Здесь код для заполнения данных на странице
            const nameDiv = document.getElementById('Name').querySelector('#data');
            const emailDiv = document.getElementById('e-mail').querySelector('#data');
            const phoneDiv = document.getElementById('phone').querySelector('#data');

            nameDiv.textContent = data.fullname || 'Не указано'; // Замените 'fullname' на имя поля в вашем JSON ответе
            emailDiv.textContent = data.email || 'Не указано'; // Добавьте поле email в модель Profile, если его нет
            phoneDiv.textContent = data.phone || 'Не указано'; // Добавьте поле phone в модель Profile, если его нет
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    }

    loadProfile(); // Вызываем функцию при загрузке страницы
});
