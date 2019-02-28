#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request

class WebScraping:
    def __init__(self):
        self.soup = ""

    def set_url(self):
        """get a url of site and save a varible"""

        return urllib.request.urlopen("https://btv.ifsp.edu.br/")

    def get_html_of_site(self):
        """docstring for get_name_of_courses"""
        url = self.set_url()
        self.soup = BeautifulSoup(url, 'html.parser')

    def get_url_of_courses(self):
        """docstring for get_name_of_courses"""
        self.get_html_of_site()
        return self.soup.find_all('a', text="Cursos")

    def web_scraping(self):
        self.get_url_of_courses()
        print(self.get_url_of_courses())

w = WebScraping()
w.web_scraping()
