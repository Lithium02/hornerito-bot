from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")

class YoutubeWeb:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
        self.url = 'https://www.youtube.com/results?search_query='


    def key_words_search_words(self, user_message):
        words = user_message.split()[0:]
        keywords = '+'.join(words)
        search_words = ' '.join(words)
        return keywords, search_words
    
    def get_video_results(self, keywords):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.url+keywords)

        youtube_data = []

        for i in range(6):
            # end_result = "No more results" string at the bottom of the page
            # this will be used to break out of the while loop
            end_result = driver.find_element(By.CSS_SELECTOR, '#message')
            driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
            # time.sleep(1) # could be removed
            # print(end_result.is_displayed())

            # once element is located, break out of the loop
            if end_result.is_displayed():
                break

        #print('Extracting results. It might take a while...')

        for result in driver.find_elements(By.CSS_SELECTOR, '.text-wrapper.style-scope.ytd-video-renderer'):
            link = result.find_element(By.CSS_SELECTOR, '.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('href')

            youtube_data.append(link)


        driver.quit()
        return youtube_data
