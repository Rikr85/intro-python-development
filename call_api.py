# Use the requests library to simplify making a REST API call from Python
import requests

# We will need the json library to read the data passed back
# by the web service
import json

# We need the key to access our Computer Vision Service
SUBCRIPTION_KEY = ""

# We need the address of our Computer Vision Service
vision_service_address = "https://{endpoint}/computervision/imageanalysis:analyze?api-version=2024-02-01[&features][&model-version][&language][&smartcrops-aspect-ratios][&gender-neutral-caption]"

# Add the name of the function we want to call to the address
address = vision_service_address + "analyze"

# Accondirng to the documentation for the analyze image function
# There are three optional parameters: language, details & visualFeatures
parameters = {'visualFeatures':'Description, Color', 'language':'en'}

# Open the image file to get a file object containing the image to analyze
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, 'rb').read()

# According to the documentation for the analyze image function
# we need to specify the subcription key and the content type
# in the HTTP header. Content Type is application/octet-stream when pass
headers = {'Content-Type':'applicataion/octet-stream', 'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# According to the documentation for the analyze image function 
# we use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))