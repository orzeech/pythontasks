from emoji import emojize
from playsound import playsound
from auditok import ADSFactory, AudioEnergyValidator, StreamTokenizer, player_for

import sys


def print_emoji():
    print(emojize(":thumbs_up:"))


def play_sound():
    if len(sys.argv) < 2:
        print("You haven't specified a file to play! Now stay silent")
        sys.exit()
    playsound(sys.argv[1])


if __name__ == '__main__':
    print("Hello, I'm using some libraries today")
    # print_emoji()
    # play_sound()
    # record = True so that we'll be able to rewind the source.
    # max_time = 10: read 10 seconds from the microphone
    asource = ADSFactory.ads(record=True, max_time=10)
    validator = AudioEnergyValidator(sample_width=asource.get_sample_width(), energy_threshold=80)
    tokenizer = StreamTokenizer(validator=validator, min_length=20, max_length=250, max_continuous_silence=30)
    player = player_for(asource)

    def echo(data, start, end):
        print("Acoustic activity at: {0}--{1}".format(start, end))
        # player.play(''.join(data))
    asource.open()
    tokenizer.tokenize(asource, callback=echo)

