from model import Model
from view import LoginView, MainView
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QHBoxLayout, QWidget

#, el archivo controller.py es responsable de manejar la lógica de la aplicación y la interacción entre el modelo y la vista. Aquí hay una explicación detallada de cómo funciona cada parte del controlador:

#Constructor __init__: Aquí se inicializan las instancias del modelo y las vistas. También se configuran las conexiones de los botones y los eventos a los métodos correspondientes del controlador.
class Controller:
    def __init__(self):
        self.model = Model()
        self.login_view = LoginView()
        self.main_view = MainView()

        self.login_view.button_login.clicked.connect(self.handle_login)
        self.main_view.button_add.clicked.connect(self.add_patient)
        self.main_view.button_logout.clicked.connect(self.logout)
        self.main_view.search_bar.textChanged.connect(self.search_patients)

    #show_login: Muestra la ventana de login.
    def show_login(self):
        self.login_view.show()

    #show_main: Muestra la ventana principal de la aplicación.
    def show_main(self):
        self.main_view.show()

    #handle_login: Este método se llama cuando el usuario intenta iniciar sesión. Verifica si las credenciales son correctas (admin123 y contrasena123). Si son correctas, cierra la ventana de login y muestra la ventana principal. Si no, muestra un mensaje de error.
    def handle_login(self):
        username = self.login_view.input_user.text()
        password = self.login_view.input_password.text()

        if username == 'admin123' and password == 'contraseña123':
            self.login_view.close()
            self.show_main()
        else:
            self.login_view.show_message('Usuario o contraseña incorrecta')

    #logout: Cierra la ventana principal y vuelve a mostrar la ventana de login
    def logout(self):
        self.main_view.close()
        self.show_login()


    #add_patient: Este método agrega un nuevo paciente. Recoge los datos de los campos de entrada. Si algún campo está vacío, muestra un mensaje de error. Intenta agregar el paciente al modelo. Si el ID ya existe, se captura una excepción ValueError y muestra un mensaje de error. Si se agrega con éxito, se limpian los campos de entrada, se muestra un mensaje de éxito y se actualiza la tabla.
    def add_patient(self):
        name = self.main_view.input_name.text()
        lastname = self.main_view.input_lastname.text()
        age = self.main_view.input_age.text()
        patient_id = self.main_view.input_id.text()

        if not (name and lastname and age and patient_id):
            self.main_view.show_message('Por favor, completa todos los campos')
            return

        try:
            self.model.add_patient({'name': name, 'lastname': lastname, 'age': age, 'id': patient_id})
            self.main_view.clear_inputs()
            self.main_view.show_message('Paciente agregado exitosamente')
            self.search_patients()  # Refresh the table
        except ValueError as e:
            self.main_view.show_message(str(e))

    #delete_patient: Este método elimina un paciente. Se llama cuando se hace clic en un botón de eliminar. Obtiene la fila del botón presionado, recupera el ID del paciente de esa fila, elimina el paciente del modelo, actualiza la tabla y muestra un mensaje de confirmación.
    def delete_patient(self):
        button = self.main_view.sender()
        if button:
            row = self.main_view.table.indexAt(button.pos()).row()
            patient_id = self.main_view.table.item(row, 3).text()
            self.model.delete_patient(patient_id)
            self.search_patients()  # Refresh the table
            self.main_view.show_message('Paciente eliminado')

    #search_patients: Este método se llama cuando el usuario escribe en la barra de búsqueda. Busca pacientes cuyo nombre comience con el texto introducido (sin distinguir entre mayúsculas y minúsculas). Limpia la tabla y muestra los resultados de la búsqueda, añadiendo un botón de eliminar para cada fila.
    def search_patients(self):
        query = self.main_view.search_bar.text()
        results = self.model.search_patients(query)
        self.main_view.table.setRowCount(0)
        for patient in results:
            row_position = self.main_view.table.rowCount()
            self.main_view.table.insertRow(row_position)
            self.main_view.table.setItem(row_position, 0, QTableWidgetItem(patient['name']))
            self.main_view.table.setItem(row_position, 1, QTableWidgetItem(patient['lastname']))
            self.main_view.table.setItem(row_position, 2, QTableWidgetItem(patient['age']))
            self.main_view.table.setItem(row_position, 3, QTableWidgetItem(patient['id']))

            # Add delete button
            delete_button = QPushButton('Eliminar')
            delete_button.clicked.connect(self.delete_patient)
            self.main_view.table.setCellWidget(row_position, 4, delete_button)
