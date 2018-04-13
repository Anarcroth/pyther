# PYTHER (Python Typing Test)

You know those tests, where you type some words as fast as you can and then it tells you how fast you typed?
Why not have the same thing in the terminal?

## Installation and launching

### Linux

Right now you can just pull this repository and launch the game from there
```bash
git clone https://github.com/Anarcroth/pyther.git && cd pyther
python3 pyther.py
```

See your scores in the auto-generated `scores` file.

If you want to blank out your scores, or have problem saving them, replace the contents of the file with just `[]`

### How To

There is one play mode. You type the words on the screen and then you check your `scores` file.
`Space` moves you to the next word. `F5` resets your current score and restars the game. `ESC` and `Ctrl+C` get you out of Pyther.
Words colored in `red` are wrong, in `blue` are correct, the current word you are typing is in `bold`.

##### Requirements
`python3` with `curses`.

## Contributions

Everybody is welcomed to contribute and expand this project. Originally started as a way to learn the language, this turned out to be quite the fun little task.

### Note
I took inspiration from other typing tests. I do not mean to steal or neglect their contribution to the typing community.
Thank you [10fastfiners](https://10fastfingers.com/typing-test/english), [typingtest](https://www.typingtest.com/), and [typingcat](https://thetypingcat.com/typing-speed-test/1m) for the countless hours of practice!
