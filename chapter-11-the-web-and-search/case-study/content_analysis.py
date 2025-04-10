# page 420
from urllib.request import urlopen
from collector import Collector

class Crawler2:
    '''Redevelop the second crawler as a class Crawler2. The set visited should be
    encapsulated as an instance variable of the Crawler2 object rather than a global variable'''
    def __init__(self):
        self.visited = set()

    def crawl(self, url: str) -> None:
        self.visited.add(url)
        links = analyze(url)

        for link in links:
            if link not in self.visited:
                try:
                    self.crawl(link)
                except:
                    pass

# frequency() from Practice Problem 11.6 (page 415)
def frequency(content: str) -> dict:
    
    counter = {}

    for word in content.split():
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1

    return counter

def analyze(url: str) -> list:
    '''prints the frequency of every word in web page url and prints and returns the list of
    http links, in absolute format, in it'''

    print('Visiting', url) # for testing

    # obtain links in a web page
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.get_links() # get a list of links

    # compute word frequencies
    content = collector.get_data() # don't have getData method
    freq = frequency(content)

    # print the frequency of every text data word in web page
    print('\n{:50} {:10} {:5}'.format('URL', 'word', 'count')) # labels
    for word in freq:
        print('{:50} {:10} {:5}'.format(url, word, freq[word]))

    # print the http links found in web page
    print('\n{:50} {:10}'.format('URL', 'link')) # labels
    for link in urls:
        print('{:50} {:10}'.format(url, link))

    return urls

if __name__ == '__main__':
    crawler3 = Crawler2()
    crawler3.crawl('https://reed.cs.depaul.edu/lperkovic/one.html')


