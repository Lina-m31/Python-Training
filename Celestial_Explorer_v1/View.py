###importing needed packages
import requests
import base64
from IPython.display import Image, display
from dotenv import load_dotenv, dotenv_values 
from IPython.core.display import HTML 
from PIL import Image as PILImage
from io import BytesIO

#function to get the moon phase for the provided date
def Moon_Phase(date):

###get the API key
    load_dotenv()
    config = dotenv_values(".env")
    api_key = config["userpass"]
    

    ### As per the API documentation we need to encode the key as below

    authString = base64.b64encode(api_key.encode('utf-8')).decode('utf-8')

    ### The base + headrs + Data  

    base= f" https://api.astronomyapi.com/api/v2/studio/moon-phase"
    headers = {
        "Authorization": f"Basic {authString}"
    }

    data = {
        "format": "png",
        "style": {
            "moonStyle": "sketch",
            "backgroundStyle": "stars",
            "backgroundColor": "red",
            "headingColor": "white",
            "textColor": "red"
        },
        "observer": {
            "latitude": 31.9544,
            "longitude": 35.9106,
            "date": f"{date}"
        },
        "view": {
            "type": "landscape-simple",
            "orientation": "south-up"
        }
    }

    ###Sending request to the website to get the moon phase for the provided date
    moon = requests.post(base, json=data, headers=headers)
    image = moon.json()


    ### Download the image
    image_url = image["data"]["imageUrl"]
    response = requests.get(image_url)
    img = PILImage.open(BytesIO(response.content))

    ### Display the image using Pillow
    img.show()



#function to get the constellation view 
def constellations(date,name="ori",style="default"):

###get the API key
    load_dotenv()
    config = dotenv_values(".env")
    api_key = config["userpass"]
    

    ### As per the API documentation we need to encode the key as below

    authString = base64.b64encode(api_key.encode('utf-8')).decode('utf-8')

    ### The base + headrs + Data  

    base= "https://api.astronomyapi.com/api/v2/studio/star-chart"
    headers = {
        "Authorization": f"Basic {authString}"
    }

    data = {
    "style": f"{style}",
    "observer": {
        "latitude": 31.9544,
        "longitude": 35.9106,
        "date": f"{date}"
    },
    "view": {
        "type": "constellation",
        "parameters": {
            "constellation": f"{name}" 
        }
    }
    }


    

    ###Sending request to the website to get the constellation image
    const = requests.post(base, json=data, headers=headers)
    image = const.json()
   
    
    
    ### Download the image
    image_url = image["data"]["imageUrl"]
    response = requests.get(image_url)
    img = PILImage.open(BytesIO(response.content))
    
    ### Display the image using Pillow
    return(img.show())





