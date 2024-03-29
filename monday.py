import speech_recognition as sr
import pyttsx3
import openai


openai.api_key = "YOUR KEY HERE"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "YOUR NAME HERE"
bot_name = "Monday"

print('----------'.center(80, '-'))

print("███╗░░░███╗░█████╗░███╗░░██╗██████╗░░█████╗░██╗░░░██╗")
print("████╗░████║██╔══██╗████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝")
print("██╔████╔██║██║░░██║██╔██╗██║██║░░██║███████║░╚████╔╝░")
print("██║╚██╔╝██║██║░░██║██║╚████║██║░░██║██╔══██║░░╚██╔╝░░")
print("██║░╚═╝░██║╚█████╔╝██║░╚███║██████╔╝██║░░██║░░░██║░░░")
print("╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░")

print('----------'.center(80, '-'))
print("NOTE: Control+C this terminal to quit")
print()

while True:
    with mic as source:
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt = user_name+":"+user_input + "\n"+bot_name+":"
    conversation += prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str =response_str.split(
        user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]

    conversation+= response_str +"\n"
    print(user_name + ": " + user_input)
    print("MONDAY: " + response_str)
    print()

    engine.say(response_str)
    engine.runAndWait()
    
