// Функция для отображения модального окна
function showModal(homeworkId) {
    const modal = document.getElementById('myModal');
    modal.style.display = 'block'; // Показываем модальное окно
    modal.setAttribute('data-id', homeworkId); // Сохраняем ID задания в атрибут модального окна
}

document.addEventListener('DOMContentLoaded', function() {
    // Обработчик отправки данных
    document.getElementById('submitBtn').addEventListener('click', function() {
    const student_answer = document.getElementById('userInput').value;
    const modal = document.getElementById('myModal');
    const hw = modal.getAttribute('data-id'); // Получаем сохраненный ID задания
    const token = localStorage.getItem('access_token');

    const dataToSend = {
        student_answer: student_answer,
        hw: hw
    };

    fetch(`/api/v1/HW/answer/${hw}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', // Указываем тип контента
            'Authorization': `Bearer ${token}` // Передаем токен в заголовке
        },
        body: JSON.stringify(dataToSend) // Преобразуем данные в строку JSON
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Сетевая ошибка или ошибка сервера');
        }
        return response.json(); // Возвращаем данные в формате JSON, если запрос успешен
    })
    .then(data => {
        console.log('Ответ сервера:', data);
        modal.style.display = 'none'; // Скрываем модальное окно после отправки
        // Здесь можно добавить дополнительные действия после успешной отправки данных
    })
    .catch(error => {
        console.error('Ошибка:', error);
        // Здесь можно обработать ошибку отправки данных
    });
});
});

// Функция для добавления обработчиков событий к кнопкам "Ответить"
function setupAnswerButtons() {
    document.querySelectorAll('.answer-button').forEach(button => {
        button.addEventListener('click', function() {
            const homeworkId = this.parentElement.getAttribute('data-id'); // Получаем ID задания из родительского элемента
            showModal(homeworkId); // Вызываем модальное окно с этим ID
        });
    });
}
