# from . import blog_generator
import json_writer
import image_scraper
import render
import appender
from llm_gateway import gateway
import re
import os
import json
from bs4 import BeautifulSoup
from acumen import about

client = gateway.select_provider("groq")
topic = input("Enter a blog topic: ")

print(f"Generating Blog in few seconds on {topic}")

blog_content = json_writer.generate_JSON(topic, client)
blog_content = blog_content.strip("```json\n").strip("```")
# json_end_index = blog_content.find('}') + 1  
# cleaned_json = blog_content[:json_end_index]
# print(f"Cleaned JSON : {cleaned_json}")


with open(f"./Data/BlogsJSON/new/{topic}.json", 'w') as json_file:
    json_file.write(blog_content)
    
print(f"New Blog Generated via AI on topic name: {topic}")
    


'''Generating HTML of new blog on given topic'''
print(f"Generating HTML")

blog_html_folder = "./Data/BlogsHTML"
old_blog_list = "./Data/Static/Topic_list.json"
processed_folder = "./Data/BlogsJSON/processed"
blog_json_folder = "./Data/BlogsJSON/new"
topic_list = os.listdir(blog_json_folder)


for i,topic in enumerate(topic_list):
    
    topic = topic.replace(".json","")
    print(f"{i+1} : Creating HTML for : {topic}")

    topic_path = f"{blog_json_folder}/{topic}.json" 
    html_file = 'Data/template.html'
    with open(html_file, 'r', encoding='utf-8') as file:
        content = BeautifulSoup(file, 'html.parser')
        
    
    with open(topic_path , 'r') as json_blog:
        blog_content = json.load(json_blog)


    # image_url = image_scraper.scrap(query=topic)
    image_url = blog_content["image_url"]
    content = render.add_image_section(image_url, content)
    
    about = about(topic)
    content = render.add_other_sections(title="About Us", soup=content, paragraphs=[about])

    for section, value in reversed(list(blog_content.items())):
        if section != "topic" and section != "image_url":
            section_title = value["title"]
            section_text = value["text"]
            content = render.add_other_sections(section_title, content, section_text)

    try:
        with open(old_blog_list, 'r') as blog_list_file:
            blog_list = json.load(blog_list_file)
    except:
        blog_list = []
   
    content = render.add_title(content, topic)
    
    new_blog_path = blog_html_folder + "/" + topic + ".html"
    with open(new_blog_path , 'w' , encoding='utf-8') as file:
        file.write(str(content))
    
    processed_json_path = f"{processed_folder}/{topic}.json"
    os.remove(topic_path)
    with open(processed_json_path, 'w') as processed_json_file:
        json.dump(blog_content, processed_json_file)
        
    print(f"Created HTML for topic : {topic} !")
    
print("New Blog is Added and Live on Website")


'''Appending New Blog into blog.html'''

html_file = 'Data/blog.html'
with open(html_file, 'r', encoding='utf-8') as file:
    content = BeautifulSoup(file, 'html.parser')

blogs_cards = content.find('div', class_ = 'col-md-8')


blog_json_folder = "./Data/BlogsJSON/new"
blog_HTML_folder = "./Data/BlogsHTML"
old_blog_list = "./Data/Static/Topic_list.json"
processed_folder = "./Data/BlogsJSON/processed"

topic_list = os.listdir(processed_folder)

try:
    with open(old_blog_list, 'r') as blog_list_file:
        blog_list = json.load(blog_list_file)
except:
    blog_list = []


for topic in reversed(topic_list):
    topic_path = f"{processed_folder}/{topic}" 
    
    with open(topic_path , 'r') as json_blog:
        blog_content = json.load(json_blog)
    intro = blog_content["introduction"]
    title = blog_content["topic"]
    intro = intro["text"]
    image_url = blog_content["image_url"]
    blog_card = appender.new_blog_card(title, image_url, intro, blog_HTML_folder="BlogsHTML")
    
    
    if blogs_cards:
        blogs_cards.insert(position=1, new_child=BeautifulSoup(blog_card, 'html.parser'))
    
    
    if (topic.replace(".json","") not in blog_list):
        blog_list.append(topic.replace(".json",""))
   
    

with open(old_blog_list, 'w') as blog_list_file:
    json.dump(blog_list , blog_list_file)

with open("./Data/index.html", 'w' , encoding='utf-8') as file:
    file.write(str(content))
    
print(f"New Blog added to blog.html")