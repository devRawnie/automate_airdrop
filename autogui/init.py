from bs4 import BeautifulSoup
from configs import get_configs
import logging
import pyautogui
import pyperclip
import requests
import webbrowser

from .utils import Position


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

    def retrieve_open_airdrops_list(self):
        res = requests.get(self.configs['coinmarketcap']['airdrop_url'])
        if res.ok:
            html = res.text
            soup = BeautifulSoup(html, 'html.parser')
            tds = soup.find_all('td', attrs={'style': 'text-align:left'})
            # TODO: write airdrops to a file
            list_of_airdrops = [(td.a['href'], td.select_one('span').text) for td in tds]
            print(list_of_airdrops)
