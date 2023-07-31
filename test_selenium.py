from selenium import webdriver
from selenium.webdriver.common.by import By


def test():

    # Configure the Chromium webdriver to work with headless mode (no GUI)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

# Initialize the driver
    driver = webdriver.Chrome(options=options)

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
        print(book_link.get_attribute('href'))

        book_links_list.append(link)

    print(book_links)
    return book_links


test()
