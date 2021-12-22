import mouse
import pygame
import keyboard
import time

class PS4Controller:
    def __init__(self):
        self.controller = None
        self.axis_data = None
        self.button_data = None

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def get_controller(self):
        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value, 2)
                    # print(self.axis_data)
                    if self.controller.get_axis(1) >= -1.0 and self.controller.get_axis(1) <= -0.85:
                        keyboard.press('w')
                    elif self.controller.get_axis(1) <= 1.0 and self.controller.get_axis(1) >= 0.85:
                        keyboard.press('s')
                    elif self.controller.get_axis(0) >= -1.0 and self.controller.get_axis(0) <= -0.85:
                        keyboard.press('a') 
                    elif self.controller.get_axis(0) <= 1.0 and self.controller.get_axis(0) >= 0.85:
                        keyboard.press('d')
                    elif self.controller.get_axis(1) >= -0.05 and self.controller.get_axis(1) <= -0.0:
                        keyboard.release('w')
                        keyboard.release('s')
                        keyboard.release('a')
                        keyboard.release('d')

                    if self.controller.get_axis(3) >= -1.0 and self.controller.get_axis(3) <= -0.85:
                        mouse.move(0, -21, absolute=False, duration=0.01)
                    elif self.controller.get_axis(3) <= 1.0 and self.controller.get_axis(3) >= 0.85:
                        mouse.move(0, 21, absolute=False, duration=0.01)
                    elif self.controller.get_axis(2) >= -1.0 and self.controller.get_axis(2) <= -0.85:
                        mouse.move(-21, 0, absolute=False, duration=0.01)
                    elif self.controller.get_axis(2) <= 1.0 and self.controller.get_axis(2) >= 0.85:
                        mouse.move(21, 0, absolute=False, duration=0.01)

                elif event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True
                    print(self.button_data)
                    if self.controller.get_button(0):
                        keyboard.press_and_release('e')
                    elif self.controller.get_button(1):
                        keyboard.press('space')
                        time.sleep(0.5)
                        keyboard.release('space')
                    elif self.controller.get_button(2):
                        keyboard.press_and_release('q')
                    elif self.controller.get_button(3):
                        keyboard.press_and_release('e')
                    elif self.controller.get_button(4):
                        mouse.wheel(1)
                    elif self.controller.get_button(5):
                        mouse.wheel(-1)
                    elif self.controller.get_button(6):
                        mouse.right_click()
                    elif self.controller.get_button(7):
                        mouse.click()
                    elif self.controller.get_button(9):
                        keyboard.press_and_release('esc')
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False