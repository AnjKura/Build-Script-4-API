#!/usr/bin/python
########################################################################################################################################################################
#Script Name :Yale University Library Voyager API Book Search Script
#Description : This script calls the open library api and searches books using the book's isbn number. The get request returns information about the book such as book title, number of pages
#Author : Anjuli Panizzi
#Error Handling: If the user makes an error in the input of the isbn or makes an error in the input of the api URL, the user will receive the status code 400 Bad Request.
                  # If the user makes a PUT/POST request but the user does not have permission to modify the resource, the user will receive a status code 403 Forbidden.If the user enters the required credentials that have the necessary permissions, the user will no longer receive status code 403.
                 # The user may enter an isbn that is not in the open library database and receive a 404 error because no data would be returned
                 #If any internal errors occur while handling the request, Status code 500 Internal Server Error would be returned.
######################################################################################################################################################################
from gettext import install
import urllib.request
import urllib.parse


#Interact with the Yale University Voyager API by initiating a GET request 
url = 'https://libapp.library.yale.edu/VoySearch/GetBibItem?isxn=9780415704953'
f = urllib.request.urlopen(url)
#Print the information returned frm the get request.
print(f.read().decode('utf-8'))
#Create a new csv file.
file = open("libraryapidata.csv")
# Download the get request information from `url` and save it locally under newly created csv file libraryapidata.csv.
with urllib.request.urlopen(url) as response, open("libraryapidata.csv", 'wb') as out_file:
    data = response.read() # a `bytes` object
    out_file.write(data)

