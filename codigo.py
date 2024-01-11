import os
import pyautogui
import time
#passos para a automação
link = 'https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf'

pyautogui.PAUSE = 1
#abrir spotligh e entrar no chrome
os.system('osascript -e "tell application \\"System Events\\" to key code 49 using {command down}"')
pyautogui.write('chrome')
pyautogui.press('return')

#digitar o endereço e ir para pagina
pyautogui.write(link)
pyautogui.press('return')

time.sleep(2)
#clicar na inscrição e digitar o numero no cnjp
pyautogui.click(x=393, y=648)
pyautogui.write('18331594000189')
pyautogui.press('tab')
pyautogui.press('tab')
#após isso só digitar o capcha e baixar o arquivo
