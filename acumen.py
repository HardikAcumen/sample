import json
from datetime import datetime
from llm_gateway import gateway

def generate_about(topic, about, categories, client):
    """
    Generates content for a specific section of the blog.
    """
    prompt = f"""Write a concise company introduction in Single Paragraph for an IT software solutions provider 
                 You are given `About` of a company and their `categories of services` 
                 make sure it should be aligned with `topic`. you have to take Company profile as a source of company information.
                 
                 topic : {topic}
                 About : {about}
                 Categories of Services : {categories}
                 
                Important: Strictly pick those categories out of all categories which are relevant to topic. Provide one single Paragraph"""
    
    response = client.chat.completions.create(
        messages= [{
                    "role":"system",
                    "content": """please do what is said to you you dump AI don't know how to behave correctly."""
                    },
                   { 
                    "role": 'user' , 
                    "content" : prompt}
                ],
        model = "llama-3.1-8b-instant",
        # model = 'llama-guard-3-8b', 
        # model = 'llama3-8b-8192',
        temperature = 0.0 ,
        max_tokens=4097
    )
    return response.choices[0].message.content

def about(topic):
    with open("Data/Acumen/acumen.json" , 'r') as about_file:
        company_info = json.load(about_file)

    about = company_info["about"]
    service_categories = company_info["service_categories"]

    client = gateway.select_provider("groq")
    about_content = generate_about(topic, about, service_categories, client)

    return about_content
    
