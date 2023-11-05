import pyttsx3
if __name__ == '__main__':
    text_to_speech = pyttsx3.init()
    while (True):
        print("Welcome to RoboSpeaker 1.1 Created By Aniket")
        word = input("Enter What You Want Me to Speak: ")
        if word == 'q':
            break
        text_to_speech.say(word)
        text_to_speech.runAndWait()




