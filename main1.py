import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string


def func():
    r = sr.Recognizer()
    isl_gif = ['any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
               'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
               'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
               'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
               'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 
               'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
               'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
               'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call me later',
               'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
               'shall we go together tomorrow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
               'what are you doing', 'what is the problem', 'what is todays date', 'what is your father do', 'what is your job',
               'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when will we go', 'where do you stay',
               'where is the bathroom', 'where is the police station', 'you are wrong','address','agra','ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
               'bihar', 'bridge', 'cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile','dasara',
               'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujarat', 'hello',
               'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
               'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
               'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
               'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
               'voice', 'wednesday', 'weight', 'please wait for sometime', 'what is your mobile number', 'what are you doing', 'are you busy']

    arr = list(string.ascii_lowercase)

    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Microphone adjusted for ambient noise. Start speaking...")

        while True:
            print("Listening...")
            try:
                
                audio = r.listen(source, timeout=2, phrase_time_limit=4)

                # Recognize the speech
                a = r.recognize_google(audio).lower()
                print(f'You Said: {a}')

                # Remove punctuation
                for c in string.punctuation:
                    a = a.replace(c, "")

                # exit condition
                if a in ['goodbye', 'good bye', 'bye']:
                    print("Goodbye! Exiting...")
                    break

                
                elif a in isl_gif:
                    display_gif(a)
                else:
                    display_letters(a)

            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
            except sr.WaitTimeoutError:
                print("Listening timed out.")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
            except Exception as e:
                print(f"An error occurred: {e}")

def display_gif(word):
    """Display relevant GIF for the recognized word"""
    class ImageLabel(tk.Label):
        """A label that displays images, and plays them if they are gifs"""
        def load(self, im):
            if isinstance(im, str):
                im = Image.open(im)
            self.loc = 0
            self.frames = []

            try:
                for i in count(1):
                    self.frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass

            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(self.frames) == 1:
                self.config(image=self.frames[0])
            else:
                self.next_frame()

        def unload(self):
            self.config(image=None)
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.loc += 1
                self.loc %= len(self.frames)
                self.config(image=self.frames[self.loc])
                self.after(self.delay, self.next_frame)

    gif_path = f'ISL_Gifs/{word}.gif'
    if os.path.exists(gif_path):
        root = tk.Tk()
        lbl = ImageLabel(root)
        lbl.pack()
        lbl.load(gif_path)
        root.mainloop()
    else:
        print(f"GIF for '{word}' not found!")

def display_letters(text):
    """Display letter images for each recognized character"""
    arr = list(string.ascii_lowercase)
    for char in text:
        if char in arr:
            image_path = f'letters/{char}.jpg'
            if os.path.exists(image_path):
                image = Image.open(image_path)
                plt.imshow(np.asarray(image))
                plt.axis('off')  
                plt.draw()
                plt.pause(0.5)  
            else:
                print(f"Image for letter '{char}' not found.")
    plt.close()


while True:
    image = "signlang.png"
    msg = "HEARING IMPAIRMENT ASSISTANT"
    choices = ["Live Voice", "All Done!"]
    reply = buttonbox(msg, image=image, choices=choices)
    
    if reply == choices[0]:
        func()
    elif reply == choices[1]:
        print("All done! Exiting the program.")
        break
