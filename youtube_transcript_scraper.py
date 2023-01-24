from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# set chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")

# initiate a webdriver object
driver = webdriver.Chrome(chrome_options=chrome_options)

# navigate to youtube video
driver.get("https://www.youtube.com/watch?v=rkv1fpWLy0Q")
driver.implicitly_wait(5000)

# 
reject_all = driver.find_element(By.XPATH, "//button[@aria-label='Reject the use of cookies and other data for the purposes described']")
reject_all.click()

# locate the next button using the xpath
next_button = driver.find_element(By.XPATH, "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button ']")
next_button.click()

# locate the next button using the xpath
show_transcript = driver.find_element(By.XPATH, "//*[@class='style-scope ytd-menu-service-item-renderer'][contains(.,'Show transcript')]")
show_transcript.click()

# locate all the instances of the xpath
elements = driver.find_elements(By.XPATH, "//yt-formatted-string[@class='segment-text style-scope ytd-transcript-segment-renderer']")

# retrieve the text inside each element
texts = [element.text for element in elements]

result = ' '.join(texts)

print(result)

# close the browser
driver.quit()