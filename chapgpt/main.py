import openai

while True:

    prompts = input("\n Introduce una pregunta: ")
    openai.api_key = "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"

    if prompts == "exit":
        break
    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompts, max_tokens=2048)

    print(completion.choices[0].text)

