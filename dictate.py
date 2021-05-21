# coding=utf-8

"""
This is an application to allowing for complete dictation of an eye exam.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""

import speech_recognition
import autogui

gui = autogui.gui_control()
recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as src:

    while True:
        try:
            audio = recognizer.adjust_for_ambient_noise(src)
            # print("Threshold Value After calibration:" +
            #       str(recognizer.energy_threshold))
            print("Please speak:")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio).lower()
            print(speech_to_txt)
        except speech_recognition.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except speech_recognition.RequestError as error:
            print(f"Could not request results from Google Speech Recognition service {error}")

        #---------------------------------------------------------------------
        # The following if-else block is for the commands I have chosen and
        # call their respective GUI action
        #---------------------------------------------------------------------
        commands = ['conjunctiva', 'cornea', 'lens', 'iris']

        if speech_to_txt in commands:
            class_method = getattr(autogui.gui_control, speech_to_txt)
            class_method(gui)
            speech_to_txt = ''
        else:
            print("Command not found.")
