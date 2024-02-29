document.addEventListener('DOMContentLoaded', function() {
    const radioYes = document.getElementById('isTeacherYes');
    const radioNo = document.getElementById('isTeacherNo');
    const subjectInputDiv = document.getElementById('subjectInput');
    const classField = document.getElementById('classField');

    radioYes.addEventListener('change', function() {
        if (radioYes.checked) {
            subjectInputDiv.style.display = 'block'; // Показываем поле для ввода предмета
            classField.style.display = 'none'; // Скрываем поле класса
        }
    });

    radioNo.addEventListener('change', function() {
        if (radioNo.checked) {
            subjectInputDiv.style.display = 'none'; // Скрываем поле для ввода предмета
            classField.style.display = 'block'; // Показываем поле класса
        }
    });
});
