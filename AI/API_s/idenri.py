import requests
import base64

# Provide the path to your input raw file
input_file_path = 'C:/Users/Emmanuel Gbodo-Otiki/Desktop/pythonprojects/AI/API_s/vv.raw'

# Read the raw file as bytes
with open(input_file_path, 'rb') as file:
    file_data = file.read()

# Convert the byte data to base64 string
base64_data = base64.b64encode(file_data).decode('utf-8')

# URL to send the POST request
url = 'https://shazam.p.rapidapi.com/songs/v2/detect'
querystring = {"timezone":"America/Chicago","locale":"en-US"}

# Define the headers and body of the POST request
headers = {
	"content-type": "text/plain",
	"X-RapidAPI-Key": "97c367ab6fmshb5057cf5d024b04p180296jsn378019c05def",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

body = base64_data

# Send the POST request
response = requests.post(url, headers=headers, data=body, params = querystring)

# Print the response
print('Response:', response.text)
