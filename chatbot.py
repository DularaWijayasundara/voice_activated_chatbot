# import openai

# openai.api_key = "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"


# def chat_with_gpt(propmt):
#     response = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo"
#         messages = [{"role": "user", "content": prompt}]

#     )
#     return response.choices[0].message.content.strip()

# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit", "bye"]:
#             break
#         response = chat_with_gpt(user_input)
#         print("Chatbot:", response)

from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="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",
) 

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)