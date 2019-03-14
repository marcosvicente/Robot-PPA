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


    def get_url_each_courses(self):
      pass 

    def get_about_to_courses(self, courses):
        url = "{0}{1}/sobre-o-curso".format(self.url_base, courses.get("href"))
        soup_about_courses = BeautifulSoup(urllib.request.urlopen(url),
                                          'html.parser')

        print(url)
        for p in soup_about_courses.find_all("div", class_="internas"):
            for text in p.find_all("p"):
                return text.get_text()
                break
        

    # def get_all_pdf_ppa(self, courses):
    #     url = "{0}{1}".format(self.url_base, courses.get("href"))
    #     url_each_courses = urllib.request.urlopen(url)
    #     soup_each_courses = BeautifulSoup(url_each_courses,
    #                                       'html.parser',
    #                                       from_encoding="iso-8859-1")
    #     link_pdf = soup_each_courses.find(
    #                         "img",
    #                         alt="Projeto Pedagógico do Curso (PPC)"
    #                     )
    #
    #     # file_zip = self.get_files_drive_ifsp(link_pdf.get("href"))
    #     # print(file_zip)
    #     # self.download_pdf(file_zip)
    #     print(url)
    #
    # def get_files_drive_ifsp(self, drive_url):
    #     url = urllib.request.urlopen(drive_url)
    #     soup_drive = BeautifulSoup(url, 'html.parser')
    #     soup_drive.find('a',  class_="button").get("href")
    #
    #
    # def download_pdf(self, url):
    #     a = urllib.request.urlopen(url)
    #     print(a)
    #     # with open(a) as f:
    #     #     f.write(request.content)


    def web_scraping(self):
        self.get_tag_name_of_page_courses()
        for courses in self.url_courses:
            print(
                self.get_about_to_courses(courses)
            )
            Database.insert_table_courses(
                self,
                courses.get_text(),
                courses.get("href"),
                self.get_about_to_courses(courses)
            )

            # self.get_all_pdf_ppa(courses)
            self.get_about_to_courses(courses)

w = WebScraping()
w.web_scraping()
