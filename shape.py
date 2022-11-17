import turtle
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.close()
skk = turtle.Turtle()

for i in range(4):
    skk.forward(50)
    skk.right(90)

turtle.done()