document.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('access_token'); // Получаем токен из localStorage

    // Функция для загрузки данных профиля и построения графиков
    function loadProfileAndBuildCharts() {
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
            buildCharts(data);
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    }

    // Функция для построения графиков
    function buildCharts(data) {
        const ctx1 = document.getElementById('diag').getContext('2d');
        const ctx2 = document.getElementById('diag2').getContext('2d');

        // График средней оценки
        new Chart(ctx1, {
            type: 'doughnut',
            data: {
                labels: ['Средняя оценка', ''],
                datasets: [{
                    data: [data.middle_mark, 5 - data.middle_mark],
                    backgroundColor: ['rgba(54, 162, 235, 0.2)', 'rgba(255, 255, 255, 0.2)'],
                    borderColor: ['rgba(54, 162, 235, 1)', 'rgba(255, 255, 255, 1)'],
                    borderWidth: 1
                }]
            },
            options: {
                circumference: 180,
                rotation: -90,
                cutout: '80%',
            }
        });

        // График предмета с минимальной средней оценкой
        new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: [data.subject_with_min_average],
                datasets: [{
                    label: 'Минимальная средняя оценка по предмету',
                    data: [data.middle_mark], // предполагается, что middle_mark - это оценка по предмету с минимальной средней
                    backgroundColor: ['rgba(255, 99, 132, 0.2)'],
                    borderColor: ['rgba(255, 99, 132, 1)'],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    loadProfileAndBuildCharts(); // Вызываем функцию при загрузке страницы
});
