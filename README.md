# Lichess Speech Recognition
Simple Speech Recognition script to play Lichess.org handsfree.

## Setup
1) Run the following command (*one-time thing*):
```
pip install gTTS playsound pynput SpeechRecognition
```
2) On [lichess](https://lichess.org), enable 'Settings > Game behaviour > Input moves with the keyboard' (*one-time thing*).
3) Run main.py, and say "enable".
4) Start a chess game, and say e.g. "**Nicholas frank 3**" for "**Nf3**" or "**Queen takes Emily 5**" for "**Qxe5**".

## Supported names
**R** = Rook, Robert<br>
**N** = Knight, Nicholas<br>
**B** = Bishop<br>
**Q** = Queen<br>
**K** = King, Kevin<br>
**a** = Adam<br>
**b** = Benjamin<br>
**c** = Charles<br>
**d** = David<br>
**e** = Emily<br>
**f** = Frank<br>
**g** = George<br>
**h** = Henry<br>
**x** = takes<br>
**O-O** = castle king side<br>
**O-O-O** = castle queen side

## Note
- Script has only been tested on Linux.
