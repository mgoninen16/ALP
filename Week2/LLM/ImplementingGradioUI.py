import gradio as gr
from huggingface_hub.inference_api import InferenceApi
import os

apiKey = os.environ["hfKey"]
inference = InferenceApi(repo_id="gpt2-large", token=apiKey)

def chat(input, max_length):
    topPparameters = {"max_length": max_length, "top_p": 0.95, "do_sample": True}
    topKparameters = {"max_length": max_length, "top_p": 0.95, "do_sample": True}
    conSearch = {"max_length": max_length, "penalty_alpha": 0.6, "top_k": 6, "do_sample": True}
    resultDet = inference(input)
    resultP = inference(input, topPparameters)
    resultK = inference(input, topKparameters)
    resultCon = inference(input, conSearch)
    return resultDet, resultP, resultK, resultCon

demo = gr.Interface(
    fn=chat,
    inputs=["text", gr.Slider(0, 200)],
    outputs=["text", "text", "text", "text"],
)
demo.launch(share = True, debug = True)