
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test():

    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('http://www.neuralnine.com/')

    driver.maximize_window()

    links = driver.find_elements("xpath", "//a[@href]")

    for link in links:
        if "Books" in link.get_attribute('innerHTML'):
            link.click()
            break

    book_links = driver.find_elements("xpath", 
                                    "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1' )]]][count(.//a)=2]//a")
    


    book_links_list = []  # Your list to store the book links

    for book_link in book_links:
        link = book_link.get_attribute('href')
        print (book_link.get_attribute('href'))

        book_links_list.append(link)

    print (book_links)
    return book_links

test()


