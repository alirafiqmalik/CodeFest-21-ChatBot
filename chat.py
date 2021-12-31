#!/usr/bin/env python

from chatbot import *
import sys

model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

if(len(sys.argv) > 1):
    print(chatbot_response(sys.argv))
else:   
    print("Not working")