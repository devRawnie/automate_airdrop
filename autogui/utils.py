import json
import pyautogui
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

class Position:
    x = None
    y = None
    duration = None
    interval = None
    filename = 'autogui/positions.json'
    tags = {}

    def __init__(self):
        with open(self.filename, 'r') as f:
            self.tags = json.load(f)

        screenWidth, screenHeight = pyautogui.size()
        logging.info('assigning screen dimensions')
        self.width = screenWidth
        self.height = screenHeight

    def move_to(self, tag, duration=0.5, interval=0.2):
        x, y = self.xy_from_tag(tag)
        pyautogui.click(x, y, duration=duration, interval=interval)

    def scroll(self, tag, clicks):
        x, y = self.xy_from_tag(tag)
        pyautogui.scroll(clicks, x, y)

    def xy_from_tag(self, tag):
        x = int(self.width // self.tags[tag]['x'])
        y = int(self.height // self.tags[tag]['y'])

        print(x,y)
        return x, y
