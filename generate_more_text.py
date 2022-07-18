import openai
import json
import os

with open('config.json', encoding='utf-8') as json_file:
    config = json.load(json_file)


output_file_name = os.path.join('out', f"{config['profileName']}.txt")
with open(output_file_name) as file:
    prompt = file.read()

openai.api_key = config['openAiToken']
response = openai.Completion().create(engine='text-davinci-002', temperature=0.9, prompt=prompt, max_tokens=3000)
with open(os.path.join('out', f'{config["profileName"]}_final_output.txt'), 'a') as output_file:
    for choice in response["choices"]:
        output_file.write(choice['text'])
        output_file.write('\n')
