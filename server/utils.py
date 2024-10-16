# utils.py
from langchain_core.prompts import ChatPromptTemplate
# from langchain_ollama.llms import OllamaLLM
from langchain_mistralai import ChatMistralAI
import requests
url = 'https://dipnlo0mruw-496ff2e9c6d22116-5000-colab.googleusercontent.com/testing'
from langchain_core.output_parsers import StrOutputParser


def ai_review(product):
    return

# Function to handle LangChain chat with product description
def langchain_chat(product_title ,product_description, question):
    myInput = {
        "product_title": product_title,
        "product_description": product_description,
        "target attributes": "Type"
    }
    # Define the JSON payload
    data = {
        "Task": "Attribute_Value_Extraction",
        "Input": myInput
    }

    response = requests.get(url, json=data)
    print(response.status_code)
    print(response.json())  # Assuming the response is in JSON format
    return response.json()["response"]
    # try:

    #     instruction = "Generate an answer to the question by utilizing the information contained in the document."
    #     # Define the LangChain template and model
    #     my_template = f"""
    #     Answer the question if it is present in the product title, bullet points or description. \
    #     If question is nonsense, trickery, or has no clear answer, I will respond with "Unknown".
    #     Start the answer with `A:` and output the answer without any explanation.

    #     Product Title: {product_title}
    #     About this item
    #     {product_description}

    #     Q: {question}
    #     """


    #     # model = OllamaLLM(model="llama3.2")
    #     model = ChatMistralAI(
    #         model="mistral-large-latest",
    #         temperature=0
    #     )

    #     prompt = ChatPromptTemplate.from_template(my_template)
    #     llm_chain =  prompt | model | StrOutputParser()

    #     llm_response = llm_chain.invoke({"product_description": product_description, "question": question, "product_title": product_title})

    #     return llm_response
    
    # except Exception as e:
    #     print(f"Error generating response from LangChain: {e}")
    #     return None
    
