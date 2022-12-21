from pynput.keyboard import Controller, Key


class Keyboard:
    def __init__(self):
        self._keyboard = Controller()

    def clear(self) -> None:
        """<CTRL> + A, followed by <BACKSPACE>"""

        self._keyboard.press(Key.ctrl.value)
        self._keyboard.press('a')
        self._keyboard.release('a')
        self._keyboard.release(Key.ctrl.value)
        self._keyboard.press(Key.backspace.value)
        self._keyboard.release(Key.backspace.value)

    def enter(self) -> None:
        """<ENTER>"""

        self._keyboard.press(Key.enter.value)
        self._keyboard.release(Key.enter.value)

    def write(self, text: str) -> None:
        """Text typed out"""

        self._keyboard.type(text)

