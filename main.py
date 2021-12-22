from gamepad.gamepad import GamePad

if __name__ == '__main__':

    gamepad = GamePad()

    while True:
        gamepad.get_event()
