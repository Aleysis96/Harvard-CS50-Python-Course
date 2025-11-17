import cowsay
import pyttsx3

engine = pyttsx3.init(driverName='espeak')
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()


# Can't reproduce audio?
# If you want to reproduce audio, make sure to install eSpeak
# In your terminal run: 'sudo apt update', then 'sudo apt install espeak-ng libespeak1'
# Remember to install the libreries before hand, 'pip install pyttsx3', 'pip install cowsay'
# if issue persist, try google for other libreries or solutions.

