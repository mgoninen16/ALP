import gradio as gr
import openai
def generate(input):
  openai.api_key = "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"
  response = openai.Completion.create(model="text-davinci-003",
                                      prompt="Imagine a world where " + input + " is the norm. Write a story that captures the essence of this world and its inhabitants",
                                      temperature=0,
                                      max_tokens=4000,
                                      top_p=1,
                                      frequency_penalty=0,
                                      presence_penalty=0
)
  return response.choices[0]['text']

def to_gradio():
  demo = gr.Interface(fn=generate,
                      inputs=["text"],
                      outputs=["text"])
  demo.launch(debug=True, share=True)

if __name__ == "__main__":
  to_gradio()