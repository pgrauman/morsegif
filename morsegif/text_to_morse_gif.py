
import fire
import imageio


letter2morse = {"A": ".-",
                "B": "-...",
                "C": "-.-.",
                "D": "-..",
                "E": ".",
                "F": "..-.",
                "G": "--.",
                "H": "....",
                "I": "..",
                "J": ".---",
                "K": "-.-",
                "L": ".-..",
                "M": "--",
                "N": "-.",
                "O": "---",
                "P": ".--.",
                "Q": "--.-",
                "R": ".-.",
                "S": "...",
                "T": "-",
                "U": "..-",
                "V": "...-",
                "W": ".--",
                "X": "-..-",
                "Y": "-.--",
                "Z": "--..",
                "1": ".----",
                "2": "..---",
                "3": "...--",
                "4": "....-",
                "5": ".....",
                "6": "-....",
                "7": "--...",
                "8": "---..",
                "9": "----.",
                "0": "-----",
                ".": ".-.-.-",
                ",": "--..--",
                "?": "..--.."}


class MorseGif(object):
    '''
    Sometimes you want to make a gif that's blinking out a message in morse
    '''

    def __init__(self, opening_frames=5, duration=0.2):
        self.opening_frames = opening_frames
        self.duration = duration
        self.char_frames = 2
        self.dit_frames = 1
        self.dat_frames = 3
        self.space_frames = 2

    def make_gif(self, text, offimg, onimg, outgif,):
        '''
        This is the main method of the ``MorseGif``onject given two stills
        and amessage it will make a gif containing the morse

        Args:
            text (str): content of the message to be converted to morse code
            offimg (str): path to the still for the "off" portion of the code
                (no sound/signal)
            onimg (str): path to the still for the "on" portion of the code
                (sound/signal)
            outgif (str): path to where the gif output should be written
        '''
        self.on = imageio.imread(onimg)
        self.off = imageio.imread(offimg)
        self.images = [self.off for x in range(self.opening_frames)]
        self.outgif = outgif
        self._make_letter2ditdat()
        self._text_to_gif(text)

    def _make_letter2ditdat(self):
        '''
        Construct a letter to gif morse dictionary
        '''
        c2d = {".": [self.on for x in range(self.dit_frames)],
               "-": [self.on for x in range(self.dat_frames)]}

        self.letter2ditdat = {}
        for l, morse in letter2morse.items():
            tmp = []
            for c in letter2morse[l]:
                for d in c2d[c]:
                    tmp.append(d)
                tmp.append(self.off)
            self.letter2ditdat[l] = tmp
        self.letter2ditdat[' '] = [self.off for x in range(self.space_frames)]
        self.letter2ditdat['nextchar'] = [self.off for x in range(self.char_frames)]  # noqa

    def _text_to_gif(self, text):
        '''
        Actually construct the gif
        '''
        text = text.upper()
        for l in text:
            self.images += self.letter2ditdat[l]
            self.images += self.letter2ditdat['nextchar']
        imageio.mimsave(self.outgif, self.images, duration=self.duration)


if __name__ == "__main__":
    fire.Fire(MorseGif)
