import requests

url = "https://shazam.p.rapidapi.com/songs/v2/detect"

querystring = {"timezone":"America/Chicago","locale":"en-US"}

payload = "\"Generate one on your own for testing and send the body with the content-type as text/plain\""
headers = {
	"content-type": "text/plain",
	"X-RapidAPI-Key": "97c367ab6fmshb5057cf5d024b04p180296jsn378019c05def",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers, params=querystring)

print(response.json())