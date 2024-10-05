from portkey_ai import Portkey
from dotenv import load_dotenv
import os
load_dotenv()


def select_provider(provider : str):
    provider = provider.upper()
    PORTKEY_API_KEY = os.getenv("PORTKEY_API_KEY")
    VIRTUAL_KEY = os.getenv("COHERE_VIRTUAL")
    
    if(provider == "GROQ"):
        VIRTUAL_KEY = os.getenv("GROQ_VIRTUAL")
        
    client =  Portkey(
            api_key=PORTKEY_API_KEY,  
            virtual_key=VIRTUAL_KEY  
        )
    
    return client


