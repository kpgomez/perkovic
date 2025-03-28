from collector import Collector
from urllib.request import urlopen

# page 416
def crawl(url: str) -> None:
    'recursive web crawler that calls analyze() on every web page'

    # analyze() returns a list of hyperlink URLs in web page url
    links = analyze(url)

    # recursively continue crawl from every linek in links
    for link in links:
        try: # try block because link may not be valid HTML file
            crawl(link)
        except: # if exception is thrown
            pass # ignore and move on


def analyze(url: str) -> list:
    '''returns the list of http links, in absolute format, in the
    web page with URL'''
    print('Visiting', url) # for testing

    # obtain links in the web page
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.get_links() # urls is the list of links

    # analysis of web page content to be done
    return urls

if __name__ == '__main__':
    test_url = 'https://reed.cs.depaul.edu/lperkovic/one.html'
    crawl(test_url)