# page 410
from urllib.parse import urljoin
from html.parser import HTMLParser

class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self, url):
        'initializes parser, the url, and a list'
        HTMLParser.__init__(self) #super().__init__()
        self.url = url
        self.links = []
        self.data = []

    # https://chatgpt.com/c/67f7ed89-4de4-800e-be78-0c3ea8c46af8
    def handle_data(self, data):
        self.data.append(data)

    def handle_starttag(self, tag, attrs):
        'collect hyperlink URLs in their absolute format'
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http':
                        self.links.append(absolute)

    def get_data(self):
        return ''.join(self.data)
    
    def get_links(self):
        'returns hyperlinks URLs in their absolute format'
        return self.links
    