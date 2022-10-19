import pyautogui as spam
import time


lm = input("Numero de mensagens: ")

msg = input("Coloque a mensagem: ")

i = 0

time.sleep(2)

while i < int(lm):
    spam.typewrite(msg)
    spam.press("Enter")

    i += 1