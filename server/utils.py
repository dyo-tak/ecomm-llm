# utils.py
from mongo import get_product_by_id, get_product_titles
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
import pprint 
pp = pprint.PrettyPrinter(indent=4)


def get_ai_summary(product_title, product_description):
    try:
        # Define the LangChain template and model
        summary_template = f"""
        Summarize the main features and benefits of the product based on the title and description provided below.
        Ensure the summary is concise, highlighting the most important information about the product.
        Start the summary with `Summary:` and avoid unnecessary details.

        Product Title: {product_title}
        Product Description: {product_description}
        """

        model = OllamaLLM(model="llama3.2")
        prompt = ChatPromptTemplate.from_template(summary_template)
        llm_chain =  prompt | model | StrOutputParser()

        llm_response = llm_chain.invoke({"product_title": product_title, "product_description": product_description})

        return llm_response
    
    except Exception as e:
        print(f"Error generating summary from LangChain: {e}")
        return None
    

def get_matching_product(product_title, product_description):
    try:
        # Define the instruction for the LLM to follow
        instruction = """
        Given the title, description of a product, identify the similar products from `List of Products` which contains a list product titles. 
        Only return a list of products that best match or are similar to the original product. Do not write code.
        Do not provide any elaboration or explanation.
        If no product is found, respond with "No matching product found."
        """

        # Prepare the input prompt
        input_data = """
        Product Title: {product_title}
        Product Description: {product_description}
        List Of Product: {product_list}
        """



        template = f"{instruction}\n\n{input_data}"
        model = OllamaLLM(model="llama3.2")
        prompt = ChatPromptTemplate.from_template(template)
        llm_chain = prompt | model | StrOutputParser()
        
        # Call the chain to get the response
        llm_response = llm_chain.invoke({
            "product_title": product_title,
            "product_description": product_description,
            "product_list": str(get_product_titles())
        })
        return llm_response

    except Exception as e:
        print(f"Error fetching product information: {e}")
        return None



def get_product_attribute_extraction(product_title, product_description, target_attributes="type, processor, screen"):
    try:
        # Instruction for attribute extraction
        instruction = """
        Given the title, description, feature, price, and brand of a product and a set of target attributes, extract the value of each target attribute from the product information. 
        Output the extracted value and the corresponding source (e.g., title or feature) denoting where the value is extracted. Give your response in the format ```Target Attribute: Attribute Value```
        """

        # Input data to be fed to the model
        input_data = f"""
        Product Title: {product_title}
        Product Description: {product_description}
        Target Attributes: {target_attributes}
        """

        # Define the LangChain template and model
        template = f"{instruction}\n\n{input_data}"
        model = OllamaLLM(model="llama3.2")
        prompt = ChatPromptTemplate.from_template(template)
        llm_chain = prompt | model | StrOutputParser()

        # Invoke the LangChain pipeline
        llm_response = llm_chain.invoke({
            "product_title": product_title,
            "product_description": product_description,
            "target_attributes": target_attributes
        })

        return llm_response

    except Exception as e:
        print(f"Error extracting product attributes: {e}")
        return None


def ai_tasks(product_id):
    product = get_product_by_id(product_id)
    product_description = product.get('description')
    product_title = product.get('title')

    ai_summary = get_ai_summary(product_title, product_description)
    product_attribute = get_product_attribute_extraction(product_title, product_description)
    matching_products = get_matching_product(product_title, product_description)

    task_results = {
        "ai_summary": ai_summary,
        "product_attribute": product_attribute,
        "matching_products": matching_products
    }

    return task_results


# Function to handle LangChain chat with product description
def langchain_chat(product_title ,product_description, question):
    try:

        instruction = "Generate an answer to the question by utilizing the information contained in the document."
        # Define the LangChain template and model
        my_template = f"""
        Answer the question if it is present in the product title, bullet points or description. \
        If question is nonsense, trickery, or has no clear answer, I will respond with "Unknown".
        Start the answer with `A:` and output the answer without any explanation.

        Product Title: {product_title}
        About this item
        {product_description}

        Q: {question}
        """


        model = OllamaLLM(model="llama3.2")
        prompt = ChatPromptTemplate.from_template(my_template)
        llm_chain =  prompt | model | StrOutputParser()

        llm_response = llm_chain.invoke({"product_description": product_description, "question": question, "product_title": product_title})

        return llm_response
    
    except Exception as e:
        print(f"Error generating response from LangChain: {e}")
        return None

    
pp.pprint(ai_tasks("6717f4f49884470f8e9a6253"))