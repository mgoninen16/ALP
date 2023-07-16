import os
gptKey = os.environ['openAI']
import openai

def generate(input):
  openai.api_key = gptKey
  response = openai.Completion.create(model="text-davinci-003",
                                      prompt=input,
                                      temperature=0,
                                      max_tokens=4000,
                                      top_p=1,
                                      frequency_penalty=0,
                                      presence_penalty=0
)
  return response.choices[0]['text']


print("Output: " + str(generate("Where is Matthew Goninen from? Make the output between 100 and 150 words")))