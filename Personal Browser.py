import typing
import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import *



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('file:///C:/Users/Krish/Desktop/Falak%20Muscat/PRSNL%20WEB%20PAGE/FALAKMUS.html'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_button = QAction('<-', self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        forward_button = QAction('->', self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        #my_website = QAction('My Website', self)
        #my_website.triggered.connect(self.browser.setUrl(QUrl('file:///C:/Users/Krish/Desktop/Falak%20Muscat/FalMus.html')))
        #navbar.addAction(my_website) adding a navbar increases ease of use for the user and thus increase in overall rating of the application cus such things need to be taken care of before the app launches rather than added features later on.

        reload_button = QAction('R', self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        home_button = QAction('🏠', self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        google_button= QAction('GOOGLE', self)
        google_button.triggered.connect(self.navigate_google)
        navbar.addAction(google_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_UserUrl)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)


    def navigate_home(self):
        self.browser.setUrl(QUrl('file:///C:/Users/Krish/Desktop/Falak%20Muscat/PRSNL%20WEB%20PAGE/FALAKMUS.html'))

    def navigate_google(self):
        self.browser.setUrl(QUrl('http://google.com'))
    
    def navigate_UserUrl(self):
        url = 'http://' + self.url_bar.text() + '.com'
        self.browser.setUrl(QUrl(url))
    
    def update_url(self, url):
        self.url_bar.setText(url.toString())


    

app = QApplication(sys.argv)
QApplication.setApplicationName('PERSONAL BROWSER')
window = MainWindow()
app.exec_()
