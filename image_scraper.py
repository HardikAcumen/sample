import os
from pyunsplash import PyUnsplash
from dotenv import load_dotenv
import sys
load_dotenv()


UNSPLASH_ACCESS_KEY=os.getenv("UNSPLASH_ACCESS_KEY")

try:
    pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)
except:
    print("Unsplash API key not found")
    sys.exit(_ExitCode = 0)
    
    
def scrap(query:str)->str:
    photos = pu.photos(type_='random', count=1, featured=True, query=query)
    [photo] = photos.entries
    
    return photo.link_download