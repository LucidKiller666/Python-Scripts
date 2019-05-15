import urllib.request
url = input("Enter the URL\n")
name = input("Enter the name for the video\n")
name=name+".mkv"
try:
    print("Downloading starts...\n")
    urllib.request.urlretrieve(url, name)
    print("Download completed..!!")
except Exception as e:
    print(e)
