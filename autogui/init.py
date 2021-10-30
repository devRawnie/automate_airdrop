from configs import get_configs, FILE_NAME
import logging
import pyautogui
import webbrowser

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

class GUI:
    def __init__(self):
        logging.info('reading config file')
        self.configs = get_configs(FILE_NAME)
        screenWidth, screenHeight = pyautogui.size()

        logging.info('assigning screen dimensions')
        self.width = screenWidth
        self.height = screenHeight

        logging.info('opening browser')
        webbrowser.open(self.configs['coinmarketcap']['url'])
        pyautogui.sleep(5)

        logging.info('Clicking on log in button')
        log_in_button = {"x": 1059,"y": 178,"duration": 0.5, "interval": 0.2}
        pyautogui.click(**log_in_button)

        # TODO: store email password, separately
        email = ""
        logging.info(f'typing email: {email}')
        pyautogui.write(email, 0.3)
        pyautogui.press('tab')
        password = ""
        logging.info('typing password')
        pyautogui.write(password, 0.2)

        logging.info('Clicking on main login button')
        main_log_in_button = {"x": 683,"y": 556,"duration": 0.5, "interval": 0.2}
        pyautogui.click(**main_log_in_button)
        pyautogui.sleep(2)

        logging.info(f'User with email: {email}, logged in')
