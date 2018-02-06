import sys
import bs4 as bs
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

def main():
    page = Page('https://developers.google.com/speed/pagespeed/insights/?url=apparat-finlandia.ru&tab=mobile')
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    test = soup.find('p', class_='speed-report-card-score')
    print(test.text)

if __name__ == '__main__':
    main()

