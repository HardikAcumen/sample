import json
from datetime import datetime
import os
import render 
from bs4 import BeautifulSoup
import image_scraper 
import appender


# blog_json_folder = "./Data/BlogsJSON"
# blog_html_folder = "./Data/BlogsHTML"
# old_blog_list = "./Data/Static/Topic_list.json"

# topic_list = os.listdir(blog_json_folder)

# for i,topic in enumerate(topic_list):
#     topic = topic.strip(".json")
#     print(f"{i+1} : {topic}")
    
# topic_name = input("Which topic you want to create blog of from above choices ")


# topic_path = f"{blog_json_folder}/{topic}.json" 
# html_file = 'Data/template.html'
# with open(html_file, 'r', encoding='utf-8') as file:
#     content = BeautifulSoup(file, 'html.parser')
    
# with open(topic_path , 'r') as json_blog:
#     blog_content = json.load(json_blog)


# image_url = image_scraper.scrap(query=topic)
# content = render.add_image_section(image_url, content)

# for section, value in reversed(list(blog_content.items())):
#     if section != "topic":
#         print(section)
#         print(type(value))
#         # value = json.loads(value)
#         section_title = value["title"]
#         section_text = value["text"]
#         content = render.add_other_sections(section_title, content, section_text)



# try:
#     with open(old_blog_list, 'r') as blog_list_file:
#         blog_list = json.load(blog_list_file)
# except:
#     blog_list = []

# other_blogs_title = content.find('div' , class_ = 'other-articlewrap')    


# if len(blog_list) > 0:
#     content = render.other_articles(content, blog_list)


# new_blog_path = blog_html_folder + "/" + topic_name + ".html"
# with open(new_blog_path , 'w' , encoding='utf-8') as file:
#     file.write(str(content))
    
# print("Done!")
    
