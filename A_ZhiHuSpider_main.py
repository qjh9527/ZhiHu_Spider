# @Time : 2023/3/18 16:59
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ZhihuSpider import Ui_MainWindow

from create_md import create_file
from answer import answer2db


class ZhiHuSpider(QMainWindow):
    def __init__(self, parent=None):
        super(ZhiHuSpider, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 设置窗口标题
        self.setWindowTitle('爬取保存知乎答案小工具')

        # 剪切板对象
        self.clipboard = QApplication.clipboard()

        # connect
        self.ui.btn_Get_MarkDowm.clicked.connect(self.get_markdowm)
        self.ui.btn_Run.clicked.connect(self.run)
        self.ui.btn_Paste.clicked.connect(self.paste2edit)

    def run(self):
        text = self.ui.textEdit_Input.toPlainText()
        self.ui.textEdit_Input.clear()
        answer2db(text, self.ui.textBrowser_Output)

    def paste2edit(self):
        text = self.clipboard.text()
        self.ui.textEdit_Input.setText(text)

    def get_markdowm(self):
        create_file(self.ui.textBrowser_Output)
        # self.ui.textBrowser_Output.setText('Get_MarkDowm：此按钮目前无效')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ZhiHuSpider()
    window.show()
    sys.exit(app.exec())
