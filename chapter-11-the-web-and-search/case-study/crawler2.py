from urllib.request import urlopen
from collector import Collector

# Practice Problem 11.7

class Crawler2:
    '''Redevelop the second crawler as a class Crawler2. The set visited should be
    encapsulated as an instance variable of the Crawler2 object rather than a global variable'''
    def __init__(self):
        self.visited = set()

    def crawl(self, url: str) -> None:
        self.visited.add(url)
        links = self.analyze(url)

        for link in links:
            if link not in self.visited:
                self.crawl(link)
            else:
                pass

    def analyze(self, url: str) -> list:
        print('Visiting', url)

        # obtain links in the web page
        content = urlopen(url).read().decode()
        collector = Collector(url)
        collector.feed(content)
        urls = collector.get_links()

        return urls


if __name__ == '__main__':
    crawler2 = Crawler2()
    crawler2.crawl('https://reed.cs.depaul.edu/lperkovic/one.html')