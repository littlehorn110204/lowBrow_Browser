import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://github.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        x = QIcon('nightlights (3).ico')
        self.setWindowIcon(x)

        # navbar
        navbar = QToolBar("Navigation")
        navbar.setIconSize(QSize(80, 80))
        self.addToolBar(navbar)

        # navbar-buttons//back//forward//reload//home//search-box

        back_btn = QAction('≪', self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('≫', self)
        forward_btn.setStatusTip("Forward to next page")
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('❉', self)
        reload_btn.setStatusTip("Click to refresh page")
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('🏛️', self)
        home_btn.setStatusTip("Go Home")
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.httpsicon = QLabel()
        self.httpsicon.setPixmap(QPixmap(os.path.join('☣')))
        navbar.addWidget(self.httpsicon)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        stop_btn = QAction('☠', self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        self.browser.urlChanged.connect(self.update_url)
        self.browser.loadFinished.connect(self.update_title)

    def navigate_home(self):

        self.browser.setUrl(QUrl('https://duckduckgo.com'))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def update_url(self, q):
        if q.scheme() == 'https':
            # secure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join('🔒')))

        else:
            # insecure padlock icon
            self.httpsicon.setPixmap(QPixmap(os.path.join('☣')))

        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s || lowBrow Browser" % title)


app = QApplication(sys.argv)
QApplication.setApplicationName('lowBrow Browser')
window = MainWindow()
app.exec_()
