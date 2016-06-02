#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        #创建BeautifulSoup对象-----------(html_doc,'html.parser',from_encoding='utf-8')
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        #通过解析html文档字符串，找到新的满足要求的url地址
        new_urls = self._get_new_urls(page_url, soup)
        #通过解析html文档字符串，找到满足要求的内容
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        #创建set对象存储解析得到的url
        new_urls = set()
        #调用find_all方法找到满足正则表达式要求的url，并存储
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            #取出相对路径
            new_url = link['href']
            #将相对路径拼凑成绝对路径
            new_full_url = urlparse.urljoin(page_url, new_url)
            #添加进set容器中
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        #获取url
        res_data['url'] = page_url
        #获取结点文字(title)
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        #获取结点文字(summary)
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data