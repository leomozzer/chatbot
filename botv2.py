from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from selenium import webdriver
import pyautogui
import time

bot = ChatBot('Test')

conv = ['oi', 'olá', 'bom dia', 'bom dia, como vai?', 'estou bem', 'qual é o seu nome?', 'meu nome é Chatbot']

bot.set_trainer(ListTrainer)

bot.train(conv)

print('Olá, eu sou o AgropetBot, atendente virtual da AgropetSol')
print('Em que posso ajudar?')

while True:
    quest = input('Você: ')

    response = bot.get_response(quest)

    if float(response.confidence) > 0.5:
        
        print('Bot: ', response)

    else:
        print('Bot: Não entendi.')

    if quest == "!salva":
        print('Bot: Salvando...')
        usuario = input("usuário: ")
        senha = input("senha: ")
        
        
        driver = webdriver.Chrome(executable_path='C:\\Users\\Leo\\Google Drive\\Programas\\Phyton\\chatbot\\chromedriver.exe')
        driver.set_page_load_timeout(30)
        driver.get('https://github.com/leomozzer/chatbot/')
        driver.maximize_window()
        driver.implicitly_wait(20)
        pyautogui.click(1069, 146)
        time.sleep(5)
        pyautogui.click(696, 337)
        time.sleep(5)
        pyautogui.typewrite(usuario)
        pyautogui.press('tab')
        time.sleep(5)
        pyautogui.typewrite(senha)
        time.sleep(5)
        pyautogui.press('tab')
        pyautogui.press('enter')
        
        
        
        

    
