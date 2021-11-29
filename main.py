import datetime
import os
import random
import time
from threading import Thread
from tkinter import *

import PREFS
import gtts
import pyjokes
import requests
import wikipedia

default_prefs = {"lang": "en"}
prefs = PREFS.Prefs(default_prefs)


def talk(text, save=False, filename="temp", extension="mp3"):
    lang = prefs.file["lang"]
    sound = gtts.gTTS(text, lang=lang)
    sound.save(f"{filename}.{extension}")
    os.system(f"mpg123 {filename}.{extension}")
    if not save: os.remove(f"{filename}.{extension}")


def wiki(name):
    wikipedia.set_lang("en")
    talk(wikipedia.summary(name, 3))


def joke():
    talk(pyjokes.get_joke())


def quote():
    talk(requests.get("https://api.quotable.io/random").json()['content'])


def timehm():
    if int(datetime.datetime.now().strftime("%M")) < 30:
        talk(f"it's {datetime.datetime.now().strftime('%M')} paste {datetime.datetime.now().strftime('%I')}")
    else:
        talk(
            f"it's {60 - int(datetime.datetime.now().strftime('%M'))} to {1 + int(datetime.datetime.now().strftime('%I'))}")


def ressources():
    talk(
        f'{os.popen("neofetch").read().split()[91]} are used in a duration of {os.popen("neofetch").read().split()[52]} and {os.popen("neofetch").read().split()[16]}')


def wait(sec, text):
    time.sleep(sec)
    reminder(text)


def delete(name, idk):
    return name.replace(idk, '')


def reminder(text):
    window = Tk()
    window.title(datetime.datetime.now().strftime('%I:%M %p'))
    Label(window, text=text)
    window.mainloop()


def generate():
	nouns = ["bird", "clock", "boy", "plastic", "duck", "teacher", "old lady", "professor", "hamster", "dog", "cat", "fish", "robot"]
	verbs = ["kicked", "ran", "flew", "dodged", "sliced", "rolled", "died", "breathed", "slept", "killed", "wrote", "ate", "saw", "said"]
	adjectives = ["beautiful", "lazy", "professional", "lovely", "dumb", "rough", "soft", "hot", "vibrating", "slimy", "cold", "jubly"]
	adverbs = ["slowly", "elegantly", "precisely", "quickly", "sadly", "humbly", "proudly", "shockingly", "calmly", "passionately"]
	preposition = ["down", "into", "up", "on", "upon", "below", "above", "through", "across", "towards"]

	def get(name):
		return random.randint(0, len(name) - 1)
		
	def gen():
		content = f"The {adjectives[get(adjectives)]} {nouns[get(nouns)]} {adverbs[get(adverbs)]} {verbs[get(verbs)]} because some {nouns[get(nouns)]} {adverbs[get(adverbs)]} {verbs[get(verbs)]} {preposition[get(preposition)]} a {adjectives[get(adjectives)]} {nouns[get(nouns)]} which, became a {adjectives[get(adjectives)]}, {adjectives[get(adjectives)]} {nouns[get(nouns)]}."
		return content
	
	talk(gen())


def save_note(time, text):
    Thread(target=wait(time * 60, text)).start()
    Thread(target=start).start()


def guess_the_number(min, max):
    num = random.randint(int(min), int(max))
    idk = ''
    while True:
        idk = int(input('-->'))
        if idk < num:
            talk('more')
        elif idk > num:
            talk('less')
        else:
            talk("congraculations!")
		return


def start():
    [print('\n') for i in range(0, 100)]
    heya = input('->')
    if 'search' in heya:
        try:
            wiki(delete(delete(heya.split('search')[1], 'what'), 'does'))
        except  IndexError:
            idk = input('what do you want to search?\n-->')
            wiki(delete(delete(delete(idk, 'what'), 'does'), 'mean'))
    elif 'say' in heya.split():
        talk(heya.split('say ')[1])
    elif 'joke' in heya:
        joke()
    elif 'quote' in heya:
        quote()
    elif 'time' in heya:
        timehm()
    elif 'generate' in heya:
    	generate()
    elif 'ressources' in heya:
        ressources()
    elif heya == "save":
        time = float(input('after how much time would you been reminded?\n-->'))
        text = input('write your not\n-->')
        save_note(time, text)
    elif 'guess' in heya:
        try:
            try:
                guess_the_number(heya.split(' and ')[0].split()[-1], heya.split(' and ')[1].split()[0])
            except AttributeError:
                guess_the_number(heya.split()[1], heya.split()[2])
        except IndexError:
            idk = input("write the max and min number separated by a space\n-->").split()
            guess_the_number(idk[0], idk[1])

    else:
        commands = 'search joke quote time ressources guess save generate'.split()
        n = len(heya)
        for time in heya:
            for command in commands:
                if heya[0: n] == command[0: n]:
                    talk(f'did you mean {command}?')
                    start()
            n -= 1
    start()


start()
