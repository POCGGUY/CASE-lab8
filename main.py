from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, QVBoxLayout, QWidget, QRadioButton

def register():
    name = name_lineedit.text()
    phone = phone_lineedit.text()
    gender = "Мужской" if male_radio.isChecked() else "Женский"
    ege_subjects = ege_subjects_lineedit.text().split(',')
    ege_scores = ege_scores_lineedit.text()
    birthdate = birthdate_dateedit.date().toString("yyyy-MM-dd")
    passport_data = passport_lineedit.text()
    email = email_lineedit.text()

    # Проверка введенных данных (можно добавить более строгие проверки)
    if not name or not phone or not ege_subjects or not ege_scores or not birthdate or not passport_data or not email:
        QMessageBox.warning(window, "Ошибка", "Заполните все поля.")
        return

    # Проверка формата введенных данных (можно добавить более строгие проверки)
    if len(ege_subjects) != 3:
        QMessageBox.warning(window, "Ошибка", "Введите 3 предмета ЕГЭ.")
        return
    try:
        ege_scores_list = [int(score) for score in ege_scores.split(',')]
        if len(ege_scores_list) != 1:
            QMessageBox.warning(window, "Ошибка", "Введите суммарный балл по ЕГЭ.")
            return
    except ValueError:
        QMessageBox.warning(window, "Ошибка", "Некорректные данные о баллах по ЕГЭ.")
        return

    # Сохранение данных (здесь можно добавить логику сохранения в базу данных)
    # ...

    QMessageBox.information(window, "Регистрация", "Вы успешно зарегистрированы!")

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("Регистрация")

# Создание виджетов
name_label = QLabel("ФИО:")
name_lineedit = QLineEdit()

phone_label = QLabel("Номер телефона:")
phone_lineedit = QLineEdit()

gender_label = QLabel("Пол:")
male_radio = QRadioButton("Мужской")
female_radio = QRadioButton("Женский")

ege_subjects_label = QLabel("Предметы ЕГЭ (через запятую):")
ege_subjects_lineedit = QLineEdit()

ege_scores_label = QLabel("Суммарный балл за 3 экзамена:")
ege_scores_lineedit = QLineEdit()

birthdate_label = QLabel("Дата рождения:")
birthdate_dateedit = QDateEdit()

passport_label = QLabel("Паспортные данные:")
passport_lineedit = QLineEdit()

email_label = QLabel("E-mail:")
email_lineedit = QLineEdit()

register_button = QPushButton("Зарегистрироваться")
register_button.clicked.connect(register)

# Размещение виджетов на форме
layout = QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(name_lineedit)
layout.addWidget(phone_label)
layout.addWidget(phone_lineedit)
layout.addWidget(gender_label)
layout.addWidget(male_radio)
layout.addWidget(female_radio)
layout.addWidget(ege_subjects_label)
layout.addWidget(ege_subjects_lineedit)
layout.addWidget(ege_scores_label)
layout.addWidget(ege_scores_lineedit)
layout.addWidget(birthdate_label)
layout.addWidget(birthdate_dateedit)
layout.addWidget(passport_label)
layout.addWidget(passport_lineedit)
layout.addWidget(email_label)
layout.addWidget(email_lineedit)
layout.addWidget(register_button)

central_widget = QWidget()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

window.show()
app.exec_()