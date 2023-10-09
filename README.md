# Hero generator 🦸

## Overview

This is a toy gradio application that generates a comic book superhero based on a superpower description.

It leverages OpenAI `gpt-3.5-turbo` for and `DALL-E 2` for text and image generation.

## Usage

To utilize the app, you need to clone the repository, install the requirements and run the application:

```
git clone https://github.com/apiraccini/hero_generator.git
cd whisper2me
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Notes

In order to utilize the tool, you need to create a `.env` file in the root directory and store your OpenAI API Key inside!