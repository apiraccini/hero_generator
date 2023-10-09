import openai
import os
from PIL import Image
import io
from dotenv import load_dotenv
from base64 import b64decode

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

def generate_hero_description(prompt):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'system', 'content': "You are an helpful assistant, specialized in comics design."},
            {'role': 'user', 'content': f"""
I will provide you the definition of a superpower, and I want you create a superhero that has such superpower.
You are going to create a name for the hero and a brief description of its appereance and its superpower.
The description should be brief but complete enough for one to draw a sketch of the hero.
Your answer should be formatted as such: 
    NAME : hero_name 
    DESCRIPTION : hero_description.
This is the superpower <<<{prompt}>>>.
Result:
"""}
        ],
        max_tokens = 128,
        temperature = 0.6
    ).choices[0].message.content
    
    return response


def generate_hero_image(description):
    response = openai.Image.create(
        prompt = f"""
I am going to provide you with the name and description of a super hero.
I want you to create an image of the hero using its superpowers based on the description. The image should be in a comic and without any text.
Name and description: {description}
""",
        n=1,
        size="512x512",
        response_format = 'b64_json'
    )['data'][0]['b64_json']
    image = Image.open(io.BytesIO(b64decode(response)))
    return image