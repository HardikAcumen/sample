import json
from html import escape
import os
from bs4 import BeautifulSoup

'''Add intro to our blog'''
def add_image_section(img_url: str, soup: BeautifulSoup):
    insertion_point = soup.find('div' , class_ = 'blog-post')
    
    img_tag = f"""
               <div class="blog-single-imgwrap">
                <img
                    src="{img_url}"
                    width="400" height="350"
                    alt="Image not loaded"
                    title="A Software Development Company in Mumbai, India - Acumen">
                </div>
                """
    
    insertion_point.insert(position=1,new_child= BeautifulSoup(img_tag,'html.parser'))
    return soup
    
    
'''Add sections into our blog'''
def add_other_sections(title: str, soup: BeautifulSoup, paragraphs: list):
    insertion_point = soup.find('div' , class_ = 'blog-single-imgwrap')
    
    h3_tag = f"""
                <h3 class="post-contentitle">{title}</h3>
              """

    p_tags = ""
    for paragraph in paragraphs:
        p_tags += f"<p>{paragraph}</p>"
        
    section = h3_tag + p_tags
    insertion_point.insert_after(BeautifulSoup(section, 'html.parser'))
    return soup
    

def other_articles(soup : BeautifulSoup, blog_list: list):
    insertion_point = soup.find('div' , class_ = 'other-articlewrap')
    
    blog_list_element = ""
    for topic_name in blog_list:
        blog_list_element += f"""
                                <a href="{topic_name}.html">
                                    {topic_name}
                                </a>
                                """
    
    insertion_point.insert(position=1, new_child=BeautifulSoup(blog_list_element, 'html.parser'))
    
    return soup
  
def add_title(soup: BeautifulSoup, topic_name):
    
    insertion_point3 = soup.find('h2', class_ = "subheading-txt")
    insertion_point4 = soup.find('head')
    
    title3 = f"""<div class="titile">Blog - <span>{topic_name}</span></div>"""
    title4 = f"""<title>{topic_name}</title>"""
    
    insertion_point3.insert(position=2, new_child=BeautifulSoup(title3, 'html.parser'))
    insertion_point4.insert(position=6, new_child=BeautifulSoup(title4, 'html.parser'))
    
    return soup
    
'''Not using it as of now'''
def add_intro_section(intro_title: str, soup: BeautifulSoup, paragraphs: list ):
    insertion_point = soup.find('div' , class_ = 'blog-post')
    h3_tag = f"""
              <h3 class="post-title">{intro_title}</h3>
              """

    p_tags = ""
    for paragraph in paragraphs:
        p_tags += f"""<p>{paragraph}</p>
        """
    
    intro = h3_tag + p_tags
    
    insertion_point.insert(position=2, new_child=BeautifulSoup(intro, 'html.parser'))
    return soup
        
        
'''We are not using this fuction as of now.'''  
def create_html(blog_data, acumen_data):
    blog_html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link rel="stylesheet" href="/Styles/styles.css">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{escape(blog_data['topic'])}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1, h2 {{ color: #333; }}
            p {{ margin: 10px 0; }}
        </style>
    </head>
    <body>
        <h1>{escape(blog_data['topic'])}</h1>
    """
    
    for section in ['introduction', 'background', 'current_state', 'conclusion']:
        title = blog_data[section]['title']
        paragraphs = blog_data[section]['text']
        blog_html_content += f"""
        <h2>{escape(title)}</h2>
        """
        for paragraph in paragraphs:
            blog_html_content += f"<p>{escape(paragraph)}</p>\n"
    
    title = acumen_data["title"]
    paragraphs = acumen_data["paragraphs"]
    blog_html_content += f"""
        <h2>{escape(title)}</h2>
        """
    for paragraph in paragraphs:
        blog_html_content += f"<p>{escape(paragraph)}</p>\n"

    blog_html_content += """
    </body>
    </html>
    """
    
    return blog_html_content


