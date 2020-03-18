'''
Play kahoot! from terminal  https://www.kahoot.it.
    type question and  new tab will open with a google search result.
Check for updated script here https://github.com/james1mumo/python-projects/kahoot.py
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://kahoot.it")

#enter game pin then click enter
pin = input('Enter game pin: ')
driver.find_element_by_xpath('//*[@id="game-input"]').send_keys(pin)
driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/form/button').click()
#enter nickname and click 'Ok go'
nickname = input('Enter your nickname: ')
driver.find_element_by_xpath('//*[@id="nickname"]').send_keys(nickname)
driver.find_element_by_xpath('/html/body/div/div/div[1]/div/main/div/form/button').click()

def scrape_answer(quiz):
    #if quiz is 1..4 then that is the answer
    if quiz in ['1','2','3','4']:
        driver.find_element_by_xpath(f'/html/body/div/div/main/div[2]/div/button[{quiz}]').click()
    #else scrape for the answer
    else:
        driver.execute_script(f'''window.open("https://www.google.com/search?q={quiz}","_blank");''')
        quiz = input(f'\tNew answer: ')
        if quiz == 'q':
            return False
        scrape_answer(quiz)

i=0
while True:
    quiz = input(f'Enter quiz {i+1}: ')
    if quiz == 'q':
        break
    scrape_answer(quiz)
    i=i+1

#driver.quit()