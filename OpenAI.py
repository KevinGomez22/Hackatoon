from openai import OpenAI
client = OpenAI(
    api_key = "xxxxx"
)

messages = [
        {"role": "system", "content": "Eres un licenciado en RH"}
    ]

input_message= input("Esperando respuesta: ")
messages.append({"role": "user", "content": input_message})


response = client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages = messages,
    temperature = 1,
    max_tokens = 200
)

content= response.choices[0].message.content
messages.append({"role": "user", "content": content})
print(content)

input_message= input("Esperando respuesta: ")
messages.append({"role": "user", "content": input_message})