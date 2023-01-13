import pyautogui,time
from datetime import datetime
region = (957,170,1920,632)
size = (0,0,963,500)
save_dir = 'f:/print/screenshot'
interval = 10
while(True):
	localtime = datetime.now() #current time
	screenshot=pyautogui.screenshot(region) #Screen area registered, in pixels
	screenshot2=screenshot.crop(size) #Image size, in pixels
	screenshot2.save(savedir+local.strftime("%m%d%Y_%H%M%S")+'.png') #defining save directory, extension and saving image
	print('Salvando: '+savedir+local.strftime("%m%d%Y_%H%M%S")+'.png')
	time.sleep(interval) # screenshot interval
