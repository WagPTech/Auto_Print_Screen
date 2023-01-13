import pyautogui,time
from datetime import datetime
while(True):
	local = datetime.now() #data e hora atual
	foto=pyautogui.screenshot(region=(957, 170, 1920, 632)) #Área da tela que será registrada em pixels
	foto2=foto.crop((0,0,963,500)) #Tamanho da imagem em pixels
	foto2.save('f:/print/foto'+local.strftime("%m%d%Y_%H%M%S")+'.png') #Definindo local e salvando a imagem
	print('Salvando: f:/print/foto'+local.strftime("%m%d%Y_%H%M%S")+'.png')
	time.sleep(10) # Intervalo entre os prints
