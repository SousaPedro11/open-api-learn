"""
Script to run the chatbot
"""
import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_response_from_openai(text: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.7,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response


def get_question_while_not_type_stop_word():
    while True:
        question = input("Human: ")
        if question == "stop":
            break
        print("AI: ", get_response_from_openai(question)["choices"][0]["text"])


if __name__ == "__main__":
    get_question_while_not_type_stop_word()
