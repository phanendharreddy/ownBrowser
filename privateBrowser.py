import sys
from PyQt5.QtCore import QUrl, Qt, QFile, QIODevice, QTextStream
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QAction, QToolBar, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("myBrowser")
        self.setGeometry(50,50,800,600)
        
        # Enable extensions
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpUserAgent("Your custom User Agent string")
        profile.setPersistentCookiesPolicy(QWebEngineProfile.AllowPersistentCookies)
        
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        
        self.create_tab()
        
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)
        
        self.navigation_bar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.navigation_bar)
        self.navigation_bar.addWidget(self.address_bar)
        
        self.back_button = QAction("Back", self)
        self.back_button.triggered.connect(self.web_view.back)
        self.navigation_bar.addAction(self.back_button)
        
        self.forward_button = QAction("Forward", self)
        self.forward_button.triggered.connect(self.web_view.forward)
        self.navigation_bar.addAction(self.forward_button)
        
        self.refresh_button = QAction("Refresh", self)
        self.refresh_button.triggered.connect(self.web_view.reload)
        self.navigation_bar.addAction(self.refresh_button)

        self.newTabButton = QAction("New Tab", self)
        self.newTabButton.triggered.connect(self.create_tab)
        self.navigation_bar.addAction(self.newTabButton)
        
        self.load_button = QAction("Load", self)
        self.load_button.triggered.connect(self.load_url)
        self.navigation_bar.addAction(self.load_button)
        
        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.tabs)
        
        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addLayout(self.vbox_layout)
        
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.hbox_layout)
        self.setCentralWidget(self.central_widget)
        
    def create_tab(self):
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl("http://www.google.com"))
        self.tabs.addTab(self.web_view, "New Tab")
        self.tabs.setCurrentWidget(self.web_view)
        
    def close_tab(self, index):
        self.tabs.removeTab(index)
        
    def load_url(self):
        url = QUrl(self.address_bar.text())
        self.current_tab().load(url)
        
    def current_tab(self):
        return self.tabs.currentWidget()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())

