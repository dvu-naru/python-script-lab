import speech_recognition  

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as misc:
    print("Robot is listenning!")
    audio = robot_ear.listen(misc)

try: 
    you = robot_ear.recognize_google(audio)
except:
    you = ""

print(you)