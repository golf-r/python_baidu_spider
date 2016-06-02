#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
class UrlManager(object):
    def __init__(self):
        #声明两个set用于存储url
        self.new_urls = set()
        self.old_urls = set()
    #添加新的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    #添加多个url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0


    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url