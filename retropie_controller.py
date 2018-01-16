import pygame, ConfigParser

# configs path
RETROPIE_GAMEPAD_CONFIG_PATH = "/opt/retropie/configs/all/retroarch-joypads/"

class Controller:

    # buttons
    A = 0
    B = 1
    BACK = 6
    START = 7
    LEFT_STICK_BTN = 9
    RIGHT_STICK_BTN = 10

    # axes
    LEFT_STICK_X = 0
    LEFT_STICK_Y = 1

    def __init__(self, id, dead_zone = 0.15):
        """
        Initializes a controller.

        Args:
            id: The ID of the controller which must be a value from `0` to
                `pygame.joystick.get_count() - 1`
            dead_zone: The size of dead zone for the analog sticks (default 0.15)
        """

        self.joystick = pygame.joystick.Joystick(id)
        self.joystick.init()
        self.dead_zone = dead_zone

        self.left_trigger_used = False
        self.right_trigger_used = False

        self.set_mapping()

    def get_id(self):
        """
        Returns:
            The ID of the controller. This is the same as the ID passed into
            the initializer.
        """

        return self.joystick.get_id()

    def dead_zone_adjustment(self, value):
        """
        Analog sticks likely wont ever return to exact center when released. Without
        a dead zone, it is likely that a small axis value will cause game objects
        to drift. This adjusment allows for a full range of input while still
        allowing a little bit of 'play' in the dead zone.

        Returns:
            Axis value outside of the dead zone remapped proportionally onto the
            -1.0 <= value <= 1.0 range.
        """

        if value > self.dead_zone:
            return (value - self.dead_zone) / (1 - self.dead_zone)
        elif value < -self.dead_zone:
            return (value + self.dead_zone) / (1 - self.dead_zone)
        else:
            return 0

    def get_buttons(self):
        """
        Gets the state of each button on the controller.

        Returns:
            A tuple with the state of each button. 1 is pressed, 0 is unpressed.
        """

        return (self.joystick.get_button(self.A),
                self.joystick.get_button(self.B),
                self.joystick.get_button(self.X),
                self.joystick.get_button(self.Y),
                self.joystick.get_button(self.LEFT_BUMP),
                self.joystick.get_button(self.RIGHT_BUMP),
                self.joystick.get_button(self.BACK),
                self.joystick.get_button(self.START),
                self.joystick.get_button(self.GUIDE),
                self.joystick.get_button(self.LEFT_STICK_BTN),
                self.joystick.get_button(self.RIGHT_STICK_BTN))
    def get_button(self, key = ""):
        """
        Gets the state of each button on the controller.

        Returns:
            A tuple with the state of each button. 1 is pressed, 0 is unpressed.
        """

        return self.joystick.get_button(getattr(self, key))

    def get_left_stick(self):
        """
        Gets the state of the left analog stick.

        Returns:
            The x & y axes as a tuple such that

            -1 <= x <= 1 && -1 <= y <= 1

            Negative values are left and up.
            Positive values are right and down.
        """

        left_stick_x = self.dead_zone_adjustment(self.joystick.get_axis(self.LEFT_STICK_X))
        left_stick_y = self.dead_zone_adjustment(self.joystick.get_axis(self.LEFT_STICK_Y))

        return (left_stick_x, left_stick_y)

    def get_pad(self):
        """
        Gets the state of the directional pad.

        Returns:
            A tuple in the form (up, right, down, left) where each value will be
            1 if pressed, 0 otherwise. Pads are 8-directional, so it is possible
            to have up to two 1s in the returned tuple.
        """

        hat_x, hat_y = self.joystick.get_hat(0)

        up = int(hat_y == 1)
        right = int(hat_x == 1)
        down = int(hat_y == -1)
        left = int(hat_x == -1)

        return up, right, down, left

    def get_config(self, path):
        """
        Returns the config object
        """
        lines = open(path).read().split("\n")
        array = {}
        for line in lines:
            item = line.split(" = ")
            if len(item) == 2:
                array[item[0]] = item[1].replace('"', '')

        return array

    def set_mapping(self):
        map_path = RETROPIE_GAMEPAD_CONFIG_PATH + self.joystick.get_name() + '.cfg'
        remap_config = self.get_config(map_path)

        self.A = int(remap_config['input_a_btn'])
        self.B = int(remap_config['input_b_btn'])
        self.START = int(remap_config['input_start_btn'])
        self.BACK = int(remap_config['input_select_btn'])
