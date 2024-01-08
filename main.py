import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
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


class addEditCoffeeForm(QMainWindow):
    def __init__(self, parent=None, coffee_data=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)

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
