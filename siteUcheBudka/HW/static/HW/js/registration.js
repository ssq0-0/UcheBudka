document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form.form__signup');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const login = form.querySelector('[name=login]').value;
        const fullname = form.querySelector('[name="fullname"]').value;
        const email = form.querySelector('[name="email"]').value;
        const password = form.querySelector('[name="password"]').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        const isTeacher = document.getElementById('isTeacherYes').checked;
        const classNumber = document.getElementById('classField').value;
        const subjectHandling = isTeacher ? document.getElementById('subjectField').value : '';
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        if (password !== confirmPassword) {
            console.log('Пароли не совпадают');
            // Вывод сообщения об ошибке
            return;
        }

        const dataToSend = {
            username: login, // Предполагается, что username это логин
            email: email,
            fullname: fullname,
            password: password,
            class_number: classNumber,
            subject_handling: isTeacher ? subjectHandling : undefined, // Отправляем subject_handling только если это учитель
            is_teacher: isTeacher,
            is_student: !isTeacher,
        };

        fetch('/api/v1/registrations/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(dataToSend),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при регистрации');
            }
            return response.json();
        })
        .then(data => {
            console.log('Успешная регистрация', data);
            window.showSignInForm();
        })
        .catch(error => {
            console.error('Ошибка:', error);
            // Обработка ошибок регистрации
        });
    });
});
