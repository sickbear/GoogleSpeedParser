import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request

class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

url = 'https://developers.google.com/speed/pagespeed/insights/?url=apparat-fortuna.ru&tab=mobile'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')
test = soup.find('p', class_='speed-report-card-score')
print(test)
