import gradio as gr
from utils.app_utils import generate_hero_description, generate_hero_image

with gr.Blocks() as demo:

    gr.Markdown('# Hero generator\nI will assist you in create a new superhero from scratch')

    with gr.Tab(label='Brainstorming'):
        superpower = gr.Textbox(label='Superpowers', placeholder='Write one or more superpowers')
        generation_btn = gr.Button(value='Generate', size = 'sm')
        hero_description = gr.Textbox(label='Hero decription', placeholder='...')

        generation_btn.click(fn=generate_hero_description, inputs=superpower, outputs=hero_description, api_name='generate_hero_description')

    with gr.Tab(label='Generation'):
        image_btn = gr.Button(value='Create your hero')
        hero_image = gr.Image(type='pil')

        image_btn.click(fn=generate_hero_image, inputs=hero_description, outputs=hero_image)

if __name__ == '__main__':
    demo.launch()