from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox, QHBoxLayout)
from PyQt5.QtCore import Qt

class LoginView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 300, 150)
        self.layout = QVBoxLayout()

        self.label_user = QLabel('Usuario:')
        self.input_user = QLineEdit()
        self.label_password = QLabel('Contraseña:')
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton('Login')
        self.layout.addWidget(self.label_user)
        self.layout.addWidget(self.input_user)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.input_password)
        self.layout.addWidget(self.button_login)

        self.setLayout(self.layout)

    def show_message(self, message):
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.exec_()

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gestión de Pacientes')
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()

        self.label_name = QLabel('Nombre:')
        self.input_name = QLineEdit()
        self.label_lastname = QLabel('Apellido:')
        self.input_lastname = QLineEdit()
        self.label_age = QLabel('Edad:')
        self.input_age = QLineEdit()
        self.label_id = QLabel('Identificación:')
        self.input_id = QLineEdit()
        self.button_add = QPushButton('Agregar Paciente')
        self.button_logout = QPushButton('Logout')

        self.layout.addWidget(self.label_name)
        self.layout.addWidget(self.input_name)
        self.layout.addWidget(self.input_lastname)
        self.layout.addWidget(self.label_age)
        self.layout.addWidget(self.input_age)
        self.layout.addWidget(self.label_id)
        self.layout.addWidget(self.input_id)
        self.layout.addWidget(self.button_add)
        self.layout.addWidget(self.button_logout)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Nombre', 'Apellido', 'Edad', 'Identificación', ''])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Buscar por nombre...')
        self.layout.addWidget(self.search_bar)

        self.setLayout(self.layout)

    def show_message(self, message):
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.exec_()

    def clear_inputs(self):
        self.input_name.clear()
        self.input_lastname.clear()
        self.input_age.clear()
        self.input_id.clear()
