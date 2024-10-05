import dominate
import os
import json
from bs4 import BeautifulSoup

def new_title_card(title: str, intro: str, blog_HTML_folder: str):
    side_card = f"""
            <a href="./{blog_HTML_folder}/{title}.html">
                {title}
            </a>
    """
    
    return side_card


def new_blog_card(title: str, image_url : str, intro: str, blog_HTML_folder: str):
    
    card_element = f"""
            <div class="blog-post">
                <div class="blog-img">
                <img
                    height = "108px"
                    width = "204px"
                    src="{image_url}"
                    alt="{title}"
                    title="Acumen - A Software Outsourcing and Blockchain Solutions Company - India, Nordic, UK">
                </div>
                <div class="blog-cont">
                <h3 class="post-title">{title}</h3>
                <p>
                {intro[0]}
                <a
                    href="{blog_HTML_folder}/{title}.html"
                    class="readmr"> Read More...</a></p>
                </div>
            </div>
            """
            
    return card_element

def new_side_blog(blog_list:str, blog_HTML_folder: str):
    blog_list_element = ""
    for topic_name in blog_list:
        blog_list_element += f"""
                                <a href="{blog_HTML_folder}/{topic_name}.html">
                                    {topic_name}
                                </a>
                                """
            
    return blog_list_element

    


# html_file = 'Data/blog.html'
# with open(html_file, 'r', encoding='utf-8') as file:
#     content = BeautifulSoup(file, 'html.parser')



# blogs_cards = content.find('div', class_ = 'col-md-8')
# other_blogs_title = content.find('div' , class_ = 'other-articlewrap')


# blog_json_folder = "./Data/BlogsJSON"
# blog_HTML_folder = "./Data/BlogsHTML"
# topic_list = os.listdir(blog_json_folder)
# old_blog_list = "./Data/Static/Topic_list.json"

# try:
#     with open(old_blog_list, 'r') as blog_list_file:
#         blog_list = json.load(blog_list_file)
# except:
#     blog_list = []

    

# print(type(blog_list))


# for topic in topic_list:
#     topic_path = f"{blog_json_folder}/{topic}" 
#     with open(topic_path , 'r') as json_blog:
#         blog_content = json.load(json_blog)
#     intro = blog_content["introduction"]
#     title = blog_content["topic"]
#     intro = intro["text"]
    
#     blog_card = new_blog_card(title, intro, blog_HTML_folder)
#     # title_card = new_title_card(title, intro, blog_HTML_folder)
    
#     if blogs_cards:
#         blogs_cards.insert(position=1, new_child=BeautifulSoup(blog_card, 'html.parser'))
    
#     # if other_blogs_title:
#     #     other_blogs_title.insert(position=1, new_child=BeautifulSoup(title_card, 'html.parser'))
#     if (topic.strip(".json") not in blog_list):
#         blog_list.append(topic.strip(".json"))
    
    

# blog_list_element = new_side_blog(blog_list, "BlogsHTML")
# other_blogs_title.insert(position=1, new_child=BeautifulSoup(blog_list_element, 'html.parser'))


# with open(old_blog_list, 'w') as blog_list_file:
#     json.dump(blog_list , blog_list_file)

# with open("./Data/new.html", 'w' , encoding='utf-8') as file:
#     file.write(str(content))
    
# print("Done!")
    
    
    
    
    