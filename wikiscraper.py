import requests
from bs4 import BeautifulSoup

class WikiWeb:
  def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
        self.url = 'https://es.wikipedia.org/wiki/'

  def key_words_search_words(self, user_message):
    words = user_message.split()[0:]
    keywords = '_'.join(words)
    search_words = ' '.join(words)
    return keywords, search_words

  def search(self, keywords):
    response = requests.get(self.url+keywords, headers = self.headers)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result = soup.find('p')
    return result