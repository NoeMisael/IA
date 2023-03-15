import speech_recognition as sr

r= sr.Recognizer()

with sr.Microphone() as source:
    print("di algo")
    audio = r.listen(source)

    try:
        text= r.recognize_google(audio)
        print("Dijiste : {}".format(text))

    except:
        print("no entendí xD")