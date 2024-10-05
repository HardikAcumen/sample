import json
from datetime import datetime


def generate_content(topic, structure, client):
    """
    Generates content for a specific section of the blog.
    """
    prompt = f"""Write a detailed blog on `topic: {topic}', in 1000 to 1500 words. The sections of blogs are given in 
                `json : {structure}'. Write atleast two paragraphs in each section. section can have. 
                Important: Plseas do not provide extra text. No Change in json structure please."""
    
    response = client.chat.completions.create(
        messages= [{
                    "role":"system",
                    "content": """Only write json nothing extra work please do what is said to you you dump AI don't know how to behave correctly."""
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