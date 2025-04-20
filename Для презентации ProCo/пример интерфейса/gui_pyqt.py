# import sys
# import os
# os.environ["QT_QPA_PLATFORM"] = "xcb"  # Фикс для Linux-систем
#
# from PyQt6.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QHBoxLayout,
#     QLineEdit, QPushButton, QScrollArea, QLabel,
#     QSizePolicy, QSpacerItem
# )
# from PyQt6.QtCore import Qt
#
# class DynamicItem(QWidget):
#     def __init__(self, text, parent=None):
#         super().__init__(parent)
#         self.layout = QHBoxLayout(self)
#         self.label = QLabel(text)
#         self.delete_btn = QPushButton("Удалить")
#
#         # Настройка стилей
#         self.label.setStyleSheet("font-size: 14px;")
#         self.delete_btn.setStyleSheet("""
#             QPushButton {
#                 background-color: #ff4444;
#                 color: white;
#                 border-radius: 5px;
#                 padding: 5px 10px;
#             }
#             QPushButton:hover {
#                 background-color: #cc0000;
#             }
#         """)
#
#         self.layout.addWidget(self.label)
#         self.layout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
#         self.layout.addWidget(self.delete_btn)
#
#         self.delete_btn.clicked.connect(lambda: self.parent().remove_item(self))
#
# class DynamicInterface(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Динамический интерфейс PyQt6')
#         self.setGeometry(300, 300, 400, 500)
#
#         main_layout = QVBoxLayout(self)
#         main_layout.setContentsMargins(10, 10, 10, 10)
#         main_layout.setSpacing(10)
#
#         # Панель ввода
#         input_layout = QHBoxLayout()
#         self.input_field = QLineEdit()
#         self.input_field.setPlaceholderText("Введите новый элемент")
#         self.input_field.setStyleSheet("font-size: 14px; padding: 5px;")
#
#         self.add_btn = QPushButton("Добавить")
#         self.clear_btn = QPushButton("Очистить всё")
#
#         # Стилизация кнопок
#         button_style = """
#             QPushButton {
#                 background-color: #4CAF50;
#                 color: white;
#                 border: none;
#                 border-radius: 5px;
#                 padding: 8px 15px;
#                 font-size: 14px;
#             }
#             QPushButton:hover {
#                 background-color: #45a049;
#             }
#         """
#         self.add_btn.setStyleSheet(button_style)
#         self.clear_btn.setStyleSheet(button_style.replace("#4CAF50", "#f44336").replace("#45a049", "#d32f2f"))
#
#         input_layout.addWidget(self.input_field, stretch=2)
#         input_layout.addWidget(self.add_btn, stretch=1)
#         input_layout.addWidget(self.clear_btn, stretch=1)
#         input_layout.setSpacing(10)
#
#         # Область прокрутки
#         self.scroll_area = QScrollArea()
#         self.scroll_area.setWidgetResizable(True)
#
#         self.content_widget = QWidget()
# self.content_layout = QVBoxLayout(self.content_widget)
#         self.content_layout.addItem(QSpacerItem(
#             20,
#             40,
#             QSizePolicy.Policy.Minimum,
#             QSizePolicy.Policy.Expanding
#         ))
#         self.content_layout.setSpacing(8)
#
#         self.scroll_area.setWidget(self.content_widget)
#
#         main_layout.addLayout(input_layout)
#         main_layout.addWidget(self.scroll_area)
#
#         # Подключение сигналов
#         self.add_btn.clicked.connect(self.add_item)
#         self.clear_btn.clicked.connect(self.clear_items)
#         self.input_field.returnPressed.connect(self.add_item)
#
#     def add_item(self):
#         text = self.input_field.text().strip()
#         if text:
#             new_item = DynamicItem(text)
#             self.content_layout.insertWidget(self.content_layout.count()-1, new_item)
#             self.input_field.clear()
#
#     def remove_item(self, item):
#         item.setParent(None)
#         item.deleteLater()
#
#     def clear_items(self):
#         while self.content_layout.count() > 1:  # Сохраняем спейсер
#             item = self.content_layout.itemAt(0)
#             if widget := item.widget():
#                 widget.setParent(None)
#                 widget.deleteLater()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = DynamicInterface()
#     window.show()
#     sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class DynamicInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Динамический интерфейс")
        self.setGeometry(100, 100, 300, 200)

        # Создаем вертикальный макет
        layout = QVBoxLayout()

        # Создаем метку
        self.label = QLabel("Введите текст и нажмите кнопку:")
        layout.addWidget(self.label)

        # Создаем текстовое поле
        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        # Создаем кнопку
        self.button = QPushButton("Обновить текст")
        self.button.clicked.connect(self.update_label)
        layout.addWidget(self.button)

        # Устанавливаем макет для виджета
        self.setLayout(layout)

    def update_label(self):
        # Обновляем текст метки
        self.label.setText(self.text_input.text())

def main():
    app = QApplication(sys.argv)
    window = DynamicInterface()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
