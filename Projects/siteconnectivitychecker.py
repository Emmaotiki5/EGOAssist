import urllib.request
def startchecker():
    input_url = input("Input the URL of the site you want to check: ")

    def main(url):
        print("Checking connectivity")
        response = urllib.request.urlopen(url)
        print("Connected to", url, "successfully")
        print(response.getcode())

    main(input_url)
