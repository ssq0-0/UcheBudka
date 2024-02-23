document.addEventListener('DOMContentLoaded', function() {
    const token = localStorage.getItem('access_token'); // Если используется аутентификация
    fetch('/api/v1/my_hw/', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}` // Если нужна авторизация
            // Добавьте другие заголовки по необходимости
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Ошибка при получении данных');
        }
        return response.json();
    })
    .then(data => {
        const table = document.getElementById('journal-table');
        let counter = 1; // Счётчик для нумерации строк

        // Обходим объект с оценками и добавляем строки в таблицу
        for (let subject in data) {
            const marks = data[subject].join(", "); // Преобразуем массив оценок в строку

            const row = table.insertRow(); // Добавляем новую строку в таблицу

            const cellNumber = row.insertCell(0); // Ячейка для номера
            const cellSubject = row.insertCell(1); // Ячейка для предмета
            const cellMarks = row.insertCell(2); // Ячейка для оценок

            cellNumber.innerHTML = counter++;
            cellSubject.innerHTML = subject;
            cellMarks.innerHTML = marks;
        }
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
});
