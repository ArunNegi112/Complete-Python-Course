import requests
## This library is primarily used to fetch data from web be sending HTTPS requests

image = requests.get(url = 'https://www.w3schools.com/w3images/lights.jpg')    
# .get() sends the HTTP GET request and fetches data, then 'image' stores the response
# i.e The response is stored in the image variable, which is a Response object containing:
# response.content: The raw binary data of the webpage (used here).
# response.text: The decoded text of the webpage.

with open('school.jpg','wb') as file: # 'wb' is write bytes
    file.write(image.content)         # .content attribute contains the raw binary data of the content (image, json etc..)
 

