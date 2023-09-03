import pickle

import gradio as gr
import numpy as np
import tensorflow as tf

from utils import clean_text, tokenize_and_pad

# Load pre-trained TensorFlow model
model = tf.keras.models.load_model('model.h5')

# Load tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
    print(type(tokenizer))

# Constants
MAX_LEN = 300


def predict_hate_speech(text):
    # Clean the text
    cleaned_text = clean_text(text)


    # Tokenize and pad the text
    preprocessed_text = tokenize_and_pad([cleaned_text], tokenizer, MAX_LEN)

    # Make a prediction
    prediction = model.predict(preprocessed_text)

    # Assuming you have two classes: "Hate" and "Not Hate"
    if prediction > 0.5:
        result = "Hate"
    else:
        result = "Not Hate"

    return result


# Create a Gradio interface
iface = gr.Interface(
    fn=predict_hate_speech,
    inputs=gr.Textbox(label="Input Text"),
    outputs=gr.Textbox(label="Output Prediction"),
    title="Hate Speech Classification",
    description="A simple hate speech classifier. Enter a text and click submit to make a prediction."
)

# Run the Gradio app
iface.launch()
