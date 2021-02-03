from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox

def handCalc():
    print("统计按钮被点击了")
    info = textEdit.toPlainText()

    salary_above_20k = ''
    salary_below_20k = ''

    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        name, salary, age = parts


app = QApplication([])
window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle("薪资统计")

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10, 25)
textEdit.resize(300, 340)

button = QPushButton('统计', window)
button.move(360,160)
# Slot
button.clicked.connect(handCalc())

window.show()

app.exec_()