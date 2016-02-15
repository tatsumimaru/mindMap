#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import random
from parse import get_parts

PROMPT = '>'
INITIAL_PROMPT = 'May I have your name?'

class Responses:
    def response_stock(parts):
        return random.choice(["How do you feel about that?", "Then what's your favorite?", "Tell me your feeling", "So, what are you working at this day?", "So, what's in your mind?"])

    def response_noun1(parts):
        responses = ["Why do you like %s?", "What do you like most about %s?", "Tell me more about %s?"]
        if 'NN' in parts:
            return random.choice(responses) % random.choice(parts['NN'])

    def response_noun2(parts):
        if 'NN' in parts:
            noun = random.choice(parts['NN'])
            return "Well well. %s, %s, %s.. What else do you have in your mind?" % (noun, noun.title(), noun.upper())


    def response_noun1(parts):
        if 'VB' in parts:
            verb = random.choice(parts['VB'])
            day = random.choice('Mondays Wednesdays Toast Acid'.split())
            return "Wow, I love to %s too, especially on %s. When do you like to %s?" % (verb, day, verb)

output = INITIAL_PROMPT
while True:
    input = raw_input(PROMPT + output + "\n")
    if input == ["Goodbye","goodbye"]:
        print "Fine... See you later!"
        sys.exit(0)
    parts = get_parts(input)
    funcs = [f for (n,f) in Responses.__dict__.items() if callable(f)]
    while True:
        resp = random.choice(funcs)
        funcs.remove(resp)
        output = resp(parts)
        if output:
            break



