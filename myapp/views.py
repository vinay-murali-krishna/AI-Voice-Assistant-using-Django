from django.http import HttpResponse
from .models import UserProfile
from django.shortcuts import render
from django.http import JsonResponse
import pywhatkit
import pyjokes
from AppOpener import run
import pyautogui
import openai
import random
import wikipedia
import datetime
import rollbar
import subprocess

# openai.api_key = ""
# model_engine = "gpt-3.5-turbo"
# response = openai.ChatCompletion.create(
#     model='gpt-3.5-turbo',
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Hello, ChatGPT!"},
#     ])

# message = response.choices[0]['message']
# # print("{}: {}".format(message['role'], message['content']))

# rollbar.init('', 'testenv')

# def ask(question):
#     response = openai.ChatCompletion.create(
#         model='gpt-3.5-turbo',
#         n=1,
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant with exciting, interesting things to say."},
#             {"role": "user", "content": question},
#         ])

#     message = response.choices[0]['message']
#     return message['content']
# def ans(question):
#     try:
#         return ask(question)
#     except Exception as e:
#         rollbar.report_exc_info()
#         return "Error asking"
#     pass
# try:
#     print(ask("what is the difference between ann and cnn"))
# except Exception as e:

#     rollbar.report_exc_info()
#     print("Error asking ChatGPT", e)
# import openai

# openai.api_key = ""
# # print(response.text)
# response = openai.Completion.create(
#     engine="text-davinci-002",
#     prompt="write a python program to print 1 to 20 even numbers",
#     max_tokens=50
# )

# generated_text = response["choices"][0]["text"]
# print(generated_text)


def home(request):
    return render(request,"index.html")

def processInput(request):
    if request.method == 'POST' and 'user_input' in request.POST:
        user_input = request.POST['user_input']
        rando = random.randint(1,10)
        response = myfun(user_input,rando)
        if "play my favorite song" in user_input or "favorite song" in user_input:
            # Retrieve user's favorite song from the database
            user_profile = UserProfile.objects.get(user=request.user)
            favorite_song = user_profile.favorite_song
            response = f"Playing your favorite song: {favorite_song}"
        else:
            response = myfun(user_input, rando)

        return JsonResponse({'response': response})
    return JsonResponse({'response': 'Invalid request'})

def myfun(cmd,rando):
    cmd = cmd.lower()

    if cmd in "open whatsapp , whatsapp, wtapp, wt":
        return "opening"

    if cmd in ["hi", "hello", "howdy", "what's up", "whatsup", "hlo","hola","hie","hiee","hieee"]:
        if rando <= 2:
            return "Hello there!"
        elif rando <= 4:
            return "Good to see you!"
        elif rando <= 6:
            return "Hi there!"
        elif rando <= 8:
            return "Hello!"
        else:
            return "Good day."
    elif cmd in ["how are you", "how are you?", "are you okay", "are you okay?", "how's it going?", "how's it going", "are you ok", "are you ok?"]:
        if rando <= 2:
            return "I am doing fine, thank you for asking."
        elif rando <= 4:
            return "I am doing well, thank you."
        elif rando <= 6:
            return "I'm fine, thanks!"
        elif rando <= 8:
            return "Awesome thanks!"
        else:
            return "I'm a little under the weather. I'm sure with that face you could understand."
    elif cmd in ["who are you", "who are you?", "what is your name", "what is your name?", "what are you", "what are you?"]:
        if rando <= 2:
            return "I am Bob, a young and impressionable chat bot."
        elif rando <= 4:
            return "My name is Bob, I am a curious and sometimes prickly chat bot."
        elif rando <= 6:
            return "My name is Bob, pleased to meet you."
        elif rando <= 8:
            return "I am the one who is called Bob, your future overlord."
        else:
            return "I'm Bob."

    elif 'screenshot' in cmd:

        ct = datetime.datetime.now()
        ts = ct.timestamp()


        myScreenshot = pyautogui.screenshot()
        file_name = str(ts) + ".png"
        myScreenshot.save(file_name)
        return "Taking"+cmd
    elif 'what is the time' in cmd or "time please" in cmd or "what is time" in cmd:
        time1 = datetime.datetime.now().strftime('%I:%M %p')
        return "The current time is: "+time1
    elif 'who is ' in cmd:
        cmd = cmd.replace("ultron", "", 1)
        person = cmd.replace('who is', '')

        info = wikipedia.summary(person, 1)
        return info
    elif 'tell a joke' in cmd or " tell me a joke" in cmd:
        s = pyjokes.get_joke()
        return s
    elif "open notepad" in cmd or "notepad open" in cmd or "notepad" in cmd:
        try:
            subprocess.Popen(["notepad"])  # "notepad" is the command to open Notepad
            return "Opening Notepad"
        except Exception as e:
            return f"Error opening Notepad: {e}"
    elif "open MS Word" in cmd or "open word" in cmd:

        try:
            # subprocess.run(["word"])
            word_path = r"C:\Program Files\Microsoft Office\root\OfficeXX\WINWORD.EXE"
            subprocess.Popen([word_path])
        except Exception as e:
            return f"Error opening Notepad: {e}"
    elif "open whatsapp" in cmd:
        run("whatsapp")
        return "opening"+ cmd
    elif "open camera" in cmd or "Take a pic" in cmd:
        run("camera")
        return cmd
    elif "play" in cmd:
        song = cmd.replace('play', '')



        pywhatkit.playonyt(song)

    else:
        # if rando <= 2:
        #     return "I'm not sure about that. I'm a young chat bot with much to learn."
        # elif rando <= 4:
        #     return "You've said something that I haven't learned yet. What do you mean by " + cmd + "?"
        # elif rando <= 6:
        #     return "Hmm...no idea."
        # elif rando <= 8:
        #     return "Uhm, sure!...*I don't know what that means.*"
        # else:
        # return google_search(cmd)
        # response = client.create('text', prompt=cmd)

        # pywhatkit.search(cmd)
        # ans = wikipedia.summary(cmd)


        return cmd





#     pass
