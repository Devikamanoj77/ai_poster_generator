import datetime
import openai
import requests
from PIL import Image, ImageFilter, ImageEnhance
import matplotlib.pyplot as plt
from io import BytesIO
import pyttsx3
from spellchecker import SpellChecker  # Import the 'SpellChecker' class

# Set the OpenAI API key
openai.api_key = "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"

# Initialize the pyttsx3 TTS engine
engine = pyttsx3.init()

# Set the voice properties for a male voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Select the male voice index

# Set the speech rate (lower value for slower speed)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  # Decrease the speech rate by 50

# Get the current local time
current_time = datetime.datetime.now()
current_day = datetime.datetime.now().strftime("%A")

# Extract the hour from the current time
current_hour = current_time.hour

# Print and speak the appropriate greeting based on the hour
if 5 <= current_hour < 12:
    greeting = "HELLO....GOOD MORNING USER, WELCOME TO PICSPOT...!"
elif 12 <= current_hour < 18:
    greeting = "HELLO...GOOD AFTERNOON USER, WELCOME TO PICSPOT...!!"
else:
    greeting = "HELLO...GOOD EVENING USER, WELCOME TO PICSPOT...!!"

print(greeting)
engine.say(greeting)
engine.runAndWait()

engine.say("Let me know what type of posters are you looking for...")
engine.runAndWait()

# Set the system prompt
system_prompt = "Generate posters that are artistic and creative."

# Get the prompt from the user
prompt = input("Enter a prompt for the posters: ")

# Combine the system prompt and user's input prompt
combined_prompt = f"{system_prompt} {prompt}"

# Generate the images
num_images = 5
response = openai.Image.create(
    prompt=combined_prompt,  # Use the combined prompt
    n=num_images,
    size="1024x1024"
)

# Download and display the filtered image
image_url = response['data'][0]['url']
image_response = requests.get(image_url)
image_data = BytesIO(image_response.content)
filtered_image = Image.open(image_data)

engine.say("Filtered Poster")
engine.runAndWait()

# Display the filtered image
plt.imshow(filtered_image)
plt.axis('off')
plt.title("Filtered Poster")
plt.show()

engine.say(f"Thank you..., Wishing you a fantastic {current_day.lower()}")
engine.runAndWait()

# Check and correct spelling in the generated text
spell = SpellChecker()
generated_text = "Filtered Poster"  # Replace with the actual generated text
words = generated_text.split()
corrected_text = " ".join(spell.correction(word) for word in words)

print("Corrected Text:", corrected_text)

engine.say(corrected_text)
engine.runAndWait()