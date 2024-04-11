import speech_recognition
import pyttsx3


recognizer = speech_recognition.Recognizer()

while True:
    try:
        print("Speak something...")
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.3)
            audio = recognizer.listen(mic)

            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(str(text))
            if text in ["quit", "exit", "bye"]:
                break

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        print("Sorry, could not understand audio.")
        continue

    except speech_recognition.RequestError as e:
        print("Could not request results; {0}".format(e))


# import speech_recognition as sr

# # Create a recognizer object
# recognizer = sr.Recognizer()

# # Capture audio from microphone
# with sr.Microphone() as source:
#     print("Speak something...")
#     audio = recognizer.listen(source)

# try:
#     print("Recognizing...")
#     # Use Google Speech Recognition
#     text = recognizer.recognize_google(audio)
#     print("You said:", text)
# except sr.UnknownValueError:
#     print("Sorry, could not understand audio.")
# except sr.RequestError as e:
#     print("Could not request results; {0}".format(e))

