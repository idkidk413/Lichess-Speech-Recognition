import gtts
import playsound
import speech_recognition as sr


def speech_to_text(language: str):
    mic = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            mic.adjust_for_ambient_noise(source)
            audio = mic.listen(source)

            try:
                yield mic.recognize_google(audio, language=language)
            except Exception as e:
                print(e)


def text_to_speech(text):
    speech = gtts.gTTS(text, lang='en')
    file_name = 'speech.mp3'
    speech.save(file_name)
    playsound.playsound(file_name)

