from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QSizePolicy

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建按钮
        button = QPushButton("Click Me")

        # 设置大小策略
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 水平扩展，垂直固定

        # 设置布局
        layout = QVBoxLayout(self)
        layout.addWidget(button)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()