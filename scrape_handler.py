from bs4 import BeautifulSoup

class Spider():

    def __init__(self, url):
        self.url = url

    def _begin_(self):
        soup = BeautifulSoup(self.url)
