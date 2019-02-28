# MorseGif

Sometimes you want to make a gif that blinks out a message in morse code. I know I do. This is a cute little script to make this dream come true. All you need is two gif stills, a message, and a convoluted reason to think you need this.

!["Hello"](img/hello.gif)

## Prerequisites
* Python3
* Virtualenv

## Installation
```
git clone https://github.com/pgrauman/morsegif.git
cd morsegif
make develop
```

## Usage

```shell
python morsegif/text_to_morse_gif.py make-gif "hello" img/open.gif img/closed.gif img/hello.gif
```