import openai

while True:

    prompts = input("\n Introduce una pregunta: ")
    openai.api_key = "Clave chatgpt"

    if prompts == "exit":
        break
    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompts, max_tokens=2048)

    print(completion.choices[0].text)

