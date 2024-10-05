## Instruction to run this script

run  `script.py` and enter any topic into input.

### 1. To put api keys for SPLASH API. create an `.env` file in root directory. 

Write API keys like this in .env folder.

```
UNSPLASH_ACCESS_KEY="L78fljR********"
```

### 2. Also create an .env file in llm-gatway folder.

llm-gateway/.env

And Write following thing

```
# Portkey
PORTKEY_API_KEY = "yzdTlg6***---***WHveig49"
# Virtual Keys
GROQ_VIRTUAL = "groq-********"
COHERE_VIRTUAL = "cohere-******"
```

# Here is Description of Each File 
acumen.py : `This code is for generating dynamic content for blog for acumen llc.`

appender.py : `This code is written to append new elements into dom structure.`

blog_generator : `This code generate json structure containing text paragraphs which can be used to construct HTML`
                 `for that topic`

image_scraper.py : `this code generates image from unsplash api for given topic`

json_writer.py : `this code contains blank json shcema defined init it is used to generate filled json with blog_generator.py`

render.py : `this code contains all utility functions which can used to add HTML element into DOM structure.`

script.py : `this code is Final Code upon running this code you can genereate and append new blog into your blogging site.`