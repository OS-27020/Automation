from selenium import webdriver

#when runnng from terminal enter "python <site name>

#chrome web driver which will launch chrome
driver = webdriver.Chrome()

#website that will launch
#you can swap out the URL for different sites
driver.get("https://motherboard.vice.com/en_us")
headlines = driver.find_elements_by_class_name("story-heading")
for headline in headlines:
    print(headline.text.strip())
