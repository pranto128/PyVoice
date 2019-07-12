



import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("speak anything: ")
    audio = r.listen(source)
try:
    print("you said \n" + r.recognize_google(audio))   
except Exception as e:
    print(e)