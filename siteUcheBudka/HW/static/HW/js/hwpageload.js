document.addEventListener('DOMContentLoaded', function () {
    const token = localStorage.getItem('access_token');
    let currentPage = 1;
    const itemsPerPage = 5;
    let allData = []; // Массив для хранения всех загруженных данных

    // Функция для загрузки всех данных
    function loadData() {
        fetch('/api/v1/HW/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при получении данных');
            }
            return response.json();
        })
        .then(data => {
            allData = data; // Сохраняем загруженные данные
            updatePage(); // Отображаем первую "страницу" данных
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    }

    // Функция для обновления отображаемых данных на текущей "странице"
    function updatePage() {
        const startIndex = (currentPage - 1) * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;
        const pageData = allData.slice(startIndex, endIndex); // Получаем данные только для текущей страницы

        const listHomeworkSection = document.getElementById('list-homework');
        listHomeworkSection.innerHTML = ''; // Очищаем предыдущие данные, чтобы отобразить новую страницу

    // Создаем и добавляем в DOM div для каждого элемента данных текущей страницы
        pageData.forEach((homework, index) => {
            const homeworkElement = document.createElement('div');
            homeworkElement.className = 'homework-item list';
            homeworkElement.setAttribute('data-id', homework.id); // Сохраняем идентификатор задания
            homeworkElement.innerHTML = `
                <p>Предмет: ${homework.school_subject}</p>
                <button class="answer-button">Ответить</button>`;
            listHomeworkSection.appendChild(homeworkElement);
        });
        setupAnswerButtons();
    }

    document.querySelector('.back').addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            updatePage();
        }
    });

    document.querySelector('.next').addEventListener('click', () => {
        const maxPage = Math.ceil(allData.length / itemsPerPage);
        if (currentPage < maxPage) {
            currentPage++;
            updatePage();
        }
    });

    loadData(); // Загрузка данных при инициализации
});

