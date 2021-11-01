from configs import get_configs
import logging
import pyautogui
from .utils import Position
import webbrowser
import pyperclip
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

class GUI:
    def __init__(self):
        logging.info('reading config file')
        self.configs = get_configs()

        self.position = Position()

        logging.info('opening browser')
        print(self.configs)
        webbrowser.open(self.configs['coinmarketcap']['url'])
        pyautogui.sleep(5)

    def login_to_coinmarket(self):
        logging.info('Clicking on log in button')
        self.position.move_to('COINMARKET__LOG_IN__1')

        # TODO: store email password, separately
        email = "rohitsdec4@gmail.com"
        logging.info(f'typing email: {email}')
        pyautogui.write(email, 0.3)
        pyautogui.press('tab')
        password = "ipsi2017#TPS"
        logging.info('typing password')
        pyautogui.write(password, 0.2)

        self.position.move_to('COINMARKET__LOG_IN__2')
        pyautogui.sleep(3)
        logging.info(f'User with email: {email}, logged in')

    def open_coindrop_page(self):
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.write(self.configs['coinmarketcap']['airdrop_url'])
        pyautogui.press('enter')
        pyautogui.sleep(2)

        pyautogui.hotkey('ctrl', 'u')
        pyautogui.sleep(1)
        pyautogui.hotkey('ctrl', 'a', inteval=0.15)
        pyautogui.hotkey('ctrl', 'c', inteval=0.15)
        text = pyperclip.paste()
        pyautogui.hotkey('ctrl', 'w', inteval=0.15)

        soup = BeautifulSoup(text, 'html.parser')
        tds = soup.find_all('td', attrs={'style': 'text-align:left'})
        # TODO: write tds to a file
        list_of_airdrops = [(td.a['href'], td.select_one('span').text) for td in tds]
        for airdrop in list_of_airdrops:
            pyautogui.hotkey('ctrl', 'l')
            pyautogui.write(self.configs['coinmarketcap'] + airdrop[0])
            pyautogui.press('enter')
            pyautogui.sleep(2)

            self.position.scroll('COINMARKET__JOIN_AIRDROP', )

