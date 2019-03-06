#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request

from database  import Database 

class WebScraping:
    def __init__(self):
        self.soup = ""
        self.url_base = "https://btv.ifsp.edu.br"
        self.url_page_courses = ""
        self.soup_courses = ""
        self.url_courses = []

    def set_url_base(self):
        """get a url of site and save a variable"""
        return urllib.request.urlopen(self.url_base)


    def get_html_of_site(self):
        """get html of site and put a variable"""
        url = self.set_url_base()
        self.soup = BeautifulSoup(url, 'html.parser')


    def get_tag_of_courses(self):
        """get tag cursos"""
        self.get_html_of_site()
        return self.soup.find_all('a', text="Cursos")


    def set_url_of_courses(self):
        for tag in self.get_tag_of_courses():
            url = tag.get("href")
        return url


    def get_page_courses(self):
        """get page of GET /cursos"""
        url = "{0}{1}".format(self.url_base, self.set_url_of_courses())
        self.url_page_courses = urllib.request.urlopen(url)
        self.soup_courses = BeautifulSoup(self.url_page_courses, 'html.parser')


    def get_tag_name_of_page_courses(self):
        """get all name of GET /cursos"""
        self.get_page_courses()
        for item_page in self.soup_courses.find_all("div", class_="item-page"):
            for ul in item_page.find_all("ul"):
                for a in ul.find_all("a"):
                    self.url_courses.append(a)


    def web_scraping(self):
        self.get_tag_name_of_page_courses()
        for courses in self.url_courses:
            Database.insert_table_courses(
                self,
                courses.get_text(),
                courses.get("href")
            )


w = WebScraping()
w.web_scraping()
