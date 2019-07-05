from speech import gen_speech
import random
from playsound import playsound
import signal
import sys
import os
from glob import glob

# I have little understanding of the signal code. I just needed it for cleanup.
# Reading the docs isn't making things too much clearer for me. Here is where I
# ripped the code from https://stackoverflow.com/questions/18114560/python-catch
# -ctrl-c-command-prompt-really-want-to-quit-y-n-resume-executi


def get_input():
    user_input = None
    while user_input is None:
        try:
            user_input = int(input("Enter a number: "))
        except ValueError as e:
            print('Please make sure you only enter numbers')
    return user_input


def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if input("\nReally quit? (y/n)> ").lower().startswith('y'):
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)


def cleanup():
    [os.remove(fi) for fi in glob('temp*')]


def main():
    tmp_file = None
    print("Set lower limit.")
    lower_limit = get_input()
    print("Set upper limit.")
    upper_limit = get_input()
    while True:
        num = random.randint(lower_limit, upper_limit)
        tmp_file = gen_speech(num, prev_file=tmp_file)  # generate speech
        playsound(tmp_file)
        user_input = get_input()
        if user_input != num:
            while user_input != num:
                print('Incorrect. Listen closely')
                playsound(tmp_file)
                user_input = get_input()
        print('Correct!')


if __name__ == '__main__':
    cleanup()
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    main()

