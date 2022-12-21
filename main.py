from keyboard_utils import Keyboard
from speech_utils import speech_to_text, text_to_speech


class Main:
    def __init__(self, write: bool, read: bool):
        self.write = write
        self.read = read
        self.keyboard = Keyboard()

    def _check_status(self, query: str) -> None:
        if 'enable' in query:
            self.write = True
            text_to_speech('successfully enabled script')
        elif 'disable' in query:
            self.write = False
            text_to_speech('successfully disabled script')

    def run(self) -> None:
        for query in speech_to_text(language='en-US'):
            self._check_status(query)

            if 'castle' in (query_lower := query.lower()):
                if all(i not in query_lower for i in ('king', 'queen')):
                    continue
                query_lower = 'OO' if 'king' in query_lower else 'OOO'
            elif 'clear' in query_lower:
                self.keyboard.clear()
            else:
                # "Charles 3" sometimes becomes "Charles II" and "Charles III"
                if 'iii' in query_lower:
                    query_lower = query_lower.replace('iii', '3')

                query_lower = query_lower.replace('rook', 'R').replace('knight', 'N').replace(
                        'night', 'N').replace('bishop', 'B').replace('queen', 'Q').replace(
                        'king', 'K').replace('takes', 'x').replace('adam', 'a').replace(
                        'benjamin', 'b').replace('david', 'd').replace('emily', 'e').replace(
                        'frank', 'f').replace('george', 'g').replace('henry', 'h').replace(
                        'one', '1').replace('two', '2').replace('three', '3').replace(
                        'four', '4').replace('five', '5').replace('six', '6').replace(
                        'seven', '7').replace('eight', '8').replace(' ', '').replace(
                        'too', '2').replace('to', '2').replace('charles', 'c').replace(
                        'for', '4').replace('robert', 'R').replace('nicholas', 'N').replace(
                        'ii', '3').replace('8th', '8').replace('nicolas', 'N').replace(
                        'kevin', 'K').replace('text', 'x').replace('rabbit', 'R').replace(
                        'vi', '6').replace('ate', '8').replace('cage', '8').replace(
                        ' v', ' 5')

            if all(i not in query_lower for i in ('enable', 'disable', 'clear')):
                if self.write:
                    if query_lower == 'OO':
                        self.keyboard.write('O-O')
                    elif query_lower == 'OOO':
                        self.keyboard.write('O-O-O')
                    else:
                        self.keyboard.write(query_lower)

                    self.keyboard.enter()

                if self.read:
                    text_to_speech(query_lower)

            print(query_lower)


if __name__ == '__main__':
    main = Main(write=False, read=False)
    main.run()

