import json
from datetime import datetime
from llm_gateway import gateway
import os
import blog_generator 
import render 
import image_scraper

def generate_JSON(topic, client):
    """
    Generates a full blog post in JSON format with sections: introduction, background, 
    current state, and conclusion.
    """
    blog_content = {
        "image_url" : "",
        "topic": f"{topic}",
        "introduction": {
            "title" : "", 
            "text" : []
            },
        "background": {
            "title" : "", 
            "text" : []
            },
        "current_state": {
            "title" : "", 
            "text" : []
            },
        "conclusion": {
            "title" : "", 
            "text" : []
            }
    }
    
    image_url = image_scraper.scrap(topic)
    blog_content["image_url"] = image_url
    
    blog_JSON = blog_generator.generate_content(topic, blog_content, client)
    return blog_JSON


# client = gateway.select_provider("groq")
# topic = input("Enter a blog topic: ")

# blog_content = generate_JSON(topic, client)
# blog_content = blog_content.strip("```json\n").strip("```")
# json_end_index = blog_content.find('}') + 1  
# cleaned_json = blog_content[:json_end_index]

# # os.makedirs(f"Data\Blogs\{topic}")
# with open(f"Data\BlogsJSON\{topic}.json", 'w') as json_file:
#     json_file.write(blog_content)
    
    