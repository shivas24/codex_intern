import speech_recognition as sr
from translate import Translator 
from monsterapi import client
import requests 
from PIL import Image
from langdetect import detect

# Initialize the client with your API key
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImE0NWIwMGNhNmM2MmU4N2VhYzAzN2VjNWU4M2ZiN2RjIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDItMTBUMTA6NDU6MjUuNTQ0MjY5In0.Y2lbJ-1xtdlzHUYfMwH51abkISP4nzUJRInzBAhkups'  
# Replace 'your-api-key' with your actual Monster API key
monster_client = client(api_key)


recognizer=sr.Recognizer()
translator=Translator(from_lang='hi-IN' ,to_lang='en-IN') 

with sr.Microphone() as source:
    print("Say something:::")
    recognizer.adjust_for_ambient_noise(source)
    audio=recognizer.listen(source)
    
    try:
        text=recognizer.recognize_google(audio, language=  'hi-IN')
        
        print("You said:",text)
           
        translated_text=translator.translate(text)
        print("Translated Text:::",f"{translated_text}")
    except sr.UnknownValueError:
        print("Can't Understand") 
    except sr.RequestError:
        print("Google API error")        

model = 'txt2img'  # Replace with the desired model name
input_data = {
'prompt': f"{translated_text}",
'negprompt': 'deformed, bad anatomy, disfigured, poorly drawn face',
'samples': 1,
'steps': 50,
'aspect_ratio': 'square',
'guidance_scale': 7.5,
'seed': 2414,
            }
print("Generating..")
result = monster_client.generate(model, input_data)

img_url=result['output'][0]

file_name="image_png"

response=requests.get(img_url)
if response.status_code==200:
    with open(file_name,"wb") as file:
        file.write(response.content)
        print(f"Image saved as {file_name}")
        img=Image.open(file_name)
        img.show()
else:
    print("Failed to download the image")


