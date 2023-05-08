import pyautogui    #lib to control the mouse and keyboard
import webbrowser   #lib to deal with the browser
import time

#configuer the browser to its library
webbrowser.register('chrome',
					 None,
					 webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'),
)
#open the required link
link='https://poe.com/ChatGPT'
webbrowser.get('chrome').open_new(link)
#wait for the page open
time.sleep(5)
#go to this positin with mouse
pyautogui.click(730,970)
#use the keypord to write a message then press enter
pyautogui.typewrite('tell me about python ')
pyautogui.press('enter')