import pyautogui    #lib to control the mouse and keyboard
import webbrowser   #lib to deal with the browser
import time

#configuer the browser to its library
webbrowser.register('chrome',
					 None,
					 webbrowser.BackgroundBrowser('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'),
)
#open the required link
link='https://app.slack.com/client/T04SFAW3J9K/C04SJ9QE4HG/shortcuts'
webbrowser.get('chrome').open_new(link)
#wait for the page open
time.sleep(10)
#go to this positin with mouse
pyautogui.click(500,930)
#use the keypord to write a message then press enter
pyautogui.typewrite('this post was written and sent using python script ;) ')
pyautogui.press('enter')