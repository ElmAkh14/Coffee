import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox


class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(800, 630)
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 781, 541))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(10, 10, 121, 23))
        self.add_button.setObjectName("add_button")
        self.edit_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_button.setGeometry(QtCore.QRect(150, 10, 121, 23))
        self.edit_button.setObjectName("edit_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(290, 10, 121, 23))
        self.delete_button.setObjectName("delete_button")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Кофе"))
        self.add_button.setText(_translate("main", "Добавить сорт"))
        self.edit_button.setText(_translate("main", "Редактировать сорт"))
        self.delete_button.setText(_translate("main", "Удалить сорт"))


class Ui_addEditCoffeeForm(object):
    def setupUi(self, addEditCoffeeForm):
        addEditCoffeeForm.setObjectName("addEditCoffeeForm")
        addEditCoffeeForm.resize(420, 280)
        self.centralwidget = QtWidgets.QWidget(addEditCoffeeForm)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.label_2.setObjectName("label_2")
        self.ground_in_grains = QtWidgets.QComboBox(self.centralwidget)
        self.ground_in_grains.setGeometry(QtCore.QRect(120, 70, 221, 20))
        self.ground_in_grains.setObjectName("ground_in_grains")
        self.ground_in_grains.addItem("")
        self.ground_in_grains.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 91, 22))
        self.label_4.setObjectName("label_4")
        self.degree_of_roasting = QtWidgets.QSpinBox(self.centralwidget)
        self.degree_of_roasting.setGeometry(QtCore.QRect(120, 40, 91, 22))
        self.degree_of_roasting.setMinimum(1)
        self.degree_of_roasting.setMaximum(1000)
        self.degree_of_roasting.setObjectName("degree_of_roasting")
        self.sort = QtWidgets.QLineEdit(self.centralwidget)
        self.sort.setGeometry(QtCore.QRect(120, 10, 221, 20))
        self.sort.setObjectName("sort")
        self.description_of_the_taste = QtWidgets.QLineEdit(self.centralwidget)
        self.description_of_the_taste.setGeometry(QtCore.QRect(120, 100, 221, 20))
        self.description_of_the_taste.setObjectName("description_of_the_taste")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 91, 22))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 91, 22))
        self.label_6.setObjectName("label_6")
        self.volume = QtWidgets.QSpinBox(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(120, 160, 91, 22))
        self.volume.setMinimum(5)
        self.volume.setMaximum(1000)
        self.volume.setObjectName("volume")
        self.cost = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.cost.setGeometry(QtCore.QRect(120, 130, 62, 22))
        self.cost.setMinimum(5.0)
        self.cost.setMaximum(100.0)
        self.cost.setObjectName("cost")
        addEditCoffeeForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addEditCoffeeForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        addEditCoffeeForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addEditCoffeeForm)
        self.statusbar.setObjectName("statusbar")
        addEditCoffeeForm.setStatusBar(self.statusbar)

        self.retranslateUi(addEditCoffeeForm)
        QtCore.QMetaObject.connectSlotsByName(addEditCoffeeForm)

    def retranslateUi(self, addEditCoffeeForm):
        _translate = QtCore.QCoreApplication.translate
        addEditCoffeeForm.setWindowTitle(_translate("addEditCoffeeForm", "Добавить запись"))
        self.pushButton.setText(_translate("addEditCoffeeForm", "Добавить"))
        self.label.setText(_translate("addEditCoffeeForm", "Название сорта"))
        self.label_2.setText(_translate("addEditCoffeeForm", "Степень обжарки"))
        self.ground_in_grains.setItemText(0, _translate("addEditCoffeeForm", "молотый"))
        self.ground_in_grains.setItemText(1, _translate("addEditCoffeeForm", "в зёрнах"))
        self.label_3.setText(_translate("addEditCoffeeForm", "Молотый/в зёрнах"))
        self.label_4.setText(_translate("addEditCoffeeForm", "Описание вкуса"))
        self.label_5.setText(_translate("addEditCoffeeForm", "Цена"))
        self.label_6.setText(_translate("addEditCoffeeForm", "Объём упаковки"))


class Coffee(QMainWindow, Ui_main):
    def __init__(self):
        super(Coffee, self).__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("release/data/coffee.sqlite")
        self.cur = self.con.cursor()
        self.coffee_data = None
        self.message = None
        self.add_coffee_widget, self.edit_coffee_widget = addEditCoffeeForm(self), addEditCoffeeForm(self)
        self.add_button.clicked.connect(self.add_coffee)
        self.edit_button.clicked.connect(self.edit_coffee)
        self.delete_button.clicked.connect(self.delete_coffee)
        self.update_table()

    def update_table(self):
        self.coffee_data = self.cur.execute("""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                                                   'Описание вкуса', 'Цена', 'Объем упаковки'])
        for i, row in enumerate(self.coffee_data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def add_coffee(self):
        self.add_coffee_widget = addEditCoffeeForm(self)
        self.add_coffee_widget.show()

    def edit_coffee(self):
        if not self.tableWidget.selectedItems():
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            rows = list(set(map(lambda x: x.row(), self.tableWidget.selectedItems())))
            ids = [self.tableWidget.item(i, 0).row() for i in rows]
            if len(ids) > 1:
                self.statusBar().showMessage('Выбрано больше 1 элемента')
            else:
                data = [self.tableWidget.item(int(ids[0]), i).text() for i in range(self.tableWidget.columnCount())]
                self.edit_coffee_widget = addEditCoffeeForm(self, data)
                self.edit_coffee_widget.show()

    def delete_coffee(self):
        try:
            rows = list(set(map(lambda x: x.row(), self.tableWidget.selectedItems())))
            ids = [self.tableWidget.item(i, 0).text() for i in rows]
            items_id = ', '.join(sorted(ids, key=lambda x: int(x)))
            assert len(items_id)
        except AssertionError:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.message = QMessageBox.question(self, '', "Действительно удалить элементы с id " + items_id + "?",
                                                QMessageBox.Yes, QMessageBox.No)
            if self.message == QMessageBox.No:
                return
            else:
                self.cur.execute(f"""DELETE FROM coffee
                WHERE id IN ({', '.join(list(map(str, items_id.split(', '))))})""")
                self.con.commit()
                self.update_table()

    def insert_result_coffee(self, data: tuple):
        self.cur.execute("""INSERT INTO coffee (variety, degree_of_roasting, ground_in_grains,
        description_of_the_taste, cost, volume)
        VALUES (?, ?, ?, ?, ?, ?)""", data)
        self.con.commit()
        self.update_table()

    def update_result_coffee(self, data: tuple):
        self.cur.execute("""UPDATE coffee
        SET variety = ?, degree_of_roasting = ?, ground_in_grains = ?, description_of_the_taste = ?,
        cost = ?, volume = ? WHERE ID = ?""", data)
        self.con.commit()
        self.update_table()

    def closeEvent(self, event):
        self.con.close()


class addEditCoffeeForm(QMainWindow, Ui_addEditCoffeeForm):
    def __init__(self, parent=None, coffee_data=None):
        super(addEditCoffeeForm, self).__init__(parent)
        self.setupUi(self)

        self.coffee_data = coffee_data
        if self.coffee_data is not None:
            self.pushButton.clicked.connect(self.edit_func)
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактировать запись')
            self.get_elem()
        else:
            self.pushButton.clicked.connect(self.add_func)

    def get_elem(self):
        self.sort.setText(self.coffee_data[1])
        self.degree_of_roasting.setValue(int(self.coffee_data[2]))
        self.ground_in_grains.setCurrentText(self.coffee_data[3])
        self.description_of_the_taste.setText(self.coffee_data[4])
        self.cost.setValue(float(self.coffee_data[5]))
        self.volume.setValue(int(self.coffee_data[6]))

    def get_adding_verdict(self):
        return all([self.sort.text(), self.description_of_the_taste.text()])

    def get_editing_verdict(self):
        return all([self.sort.text(), self.description_of_the_taste.text()])

    def add_func(self):
        if self.get_adding_verdict():
            data = (self.sort.text(), self.degree_of_roasting.value(), self.ground_in_grains.currentText(),
                    self.description_of_the_taste.text(), self.cost.value(), self.volume.value())
            self.parent().insert_result_coffee(data)
            self.statusBar().showMessage('')
            self.close()
        else:
            self.statusBar().showMessage('Неверно заполнена форма')

    def edit_func(self):
        if self.get_editing_verdict():
            data = (self.sort.text(), self.degree_of_roasting.value(), self.ground_in_grains.currentText(),
                    self.description_of_the_taste.text(), self.cost.value(), self.volume.value(),
                    int(self.coffee_data[0]))
            self.parent().update_result_coffee(data)
            self.statusBar().showMessage('')
            self.close()
        else:
            self.statusBar().showMessage('Неверно заполнена форма')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
