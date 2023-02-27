# %% [markdown]
# # AI-Translator
# This is an web app with an English/Chinese translation and grammar check function

# %% [markdown]
# install the following packages:

# %%
# !pip3 install torch==1.8.2+cu111 torchvision==0.9.2+cu111 torchaudio==0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
# !pip3 install pip==20.1.1 
# !pip3 install -U git+https://github.com/PrithivirajDamodaran/Gramformer.git
# !pip install spacy
# !python -m spacy download en
# !pip install gradio
# !pip install transformers
# !pip install errant

# %% [markdown]
# import depandancies

# %%
from gramformer import Gramformer
import spacy
import gradio as gr
from transformers import pipeline
from gramformer import Gramformer
spacy.load('en')
# from spacy.lang.en import English

# %% [markdown]
# define api for translation and grama check

# %%

def extract_str(text):
    text=str(text)
    start = text.find("{'")
    end = text.find("'}")
    return text[start+2:end]
    
def gramacorrect(sentence):
    gf = Gramformer(models=1, use_gpu=False)
    res = gf.correct(sentence) # Gramformer correct
    return extract_str(res) # Return first value in res array

def translate_zh(from_text):
    translation_pipeline = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")
    res = translation_pipeline(from_text)[0]      
    return res['translation_text']

def translate_en(from_text):
    translation_pipeline = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")
    res = translation_pipeline(from_text)[0]      
    return res['translation_text']

def generator(from_text):
    english_generator = pipeline("text-generation", model="distilgpt2")
    english_text = english_generator(from_text)[0]["generated_text"]
    return english_text

# %% [markdown]
# build interface for web app

# %%

with gr.Blocks() as demo:
    with gr.Tab("Translator"):
        gr.Markdown("""
                    #### English to Chinese.
                    """)

        with gr.Row():
            text_input1 = gr.Textbox(lines=4, placeholder="Enter sentence here...")
            chinese = gr.Textbox(lines=4, placeholder="Chinese")
        zh_button = gr.Button("RUN")
        gr.Markdown("""
                    #### Chinese to English.
                    """)

        with gr.Row():
            text_input2 = gr.Textbox(lines=4, placeholder="Enter sentence here...")
            english = gr.Textbox(lines=4, placeholder="English")
        en_button = gr.Button("RUN")            
    
    with gr.Tab("Gramachecker"):
        gr.Markdown("""
                    #### English grama checker.
                    """)
        with gr.Row():
            text_input3 = gr.Textbox(lines=4, placeholder="Enter sentence here...")
            check = gr.Textbox(lines=4, placeholder="Grama Check")
        check_button = gr.Button("RUN")

        gr.Markdown("""
                    #### English text generator.
                    """)
        with gr.Row():
            text_input4 = gr.Textbox(lines=2, placeholder="Enter sentence here...")
            txtgenerator = gr.Textbox(lines=6, placeholder="Text Generator")
        gen_button = gr.Button("RUN")    



    zh_button.click(translate_zh, inputs=text_input1, outputs=chinese)
    en_button.click(translate_en, inputs=text_input2, outputs=english)
    
    check_button.click(gramacorrect, inputs=text_input3, outputs=check)
    gen_button.click(generator, inputs=text_input4, outputs=txtgenerator)
demo.launch()


# %%



