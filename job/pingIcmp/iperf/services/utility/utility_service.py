import requests
import urllib.request
import numpy as np


class UtilityService:
    def url_downloader(url):
        response = requests.get(url)
        return (response.headers['content-type'], response.content)
            
    def image_reader(url):
            return urllib.request.urlopen(url).read()
