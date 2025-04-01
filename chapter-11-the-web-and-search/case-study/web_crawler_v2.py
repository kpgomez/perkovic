from web_crawler_v1 import analyze

visited = set()
def crawl(url: str) -> None:
    'a recursive web crawler that calls analyze() on every visited web page'

    # add url to set of visited pages
    global visited # while not necessary, warns the programmer
    visited.add(url)

    # analyze() returns a list of hyperlink URLs in web page url
    links = analyze(url)

    # recursively continue crawl from every link in links
    for link in links:
        # follow link only if not visited
        if link not in visited:
            try:
                crawl(link)
            except:
                pass


if __name__ == '__main__':
    test_url = 'https://reed.cs.depaul.edu/lperkovic/one.html'
    crawl(test_url)