#! /usr/bin/python
from gettext import install
import urllib.request
import urllib.parse



url = 'https://libapp.library.yale.edu/VoySearch/GetBibItem?isxn=9780415704953'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))

file = open("libraryapidata.csv")
# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen(url) as response, open("libraryapidata.csv", 'wb') as out_file:
    data = response.read() # a `bytes` object
    out_file.write(data)
import subprocess

