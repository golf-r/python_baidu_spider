#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# 爬虫调度端

import url_manager
import html_downloader
import html_outputer
import html_parser

class SpiderMain(object):
    #构造函数
    def __init__(self):
        #声明管理器对象
        self.urls = url_manager.UrlManager()
        #声明下载器对象
        self.downloader = html_downloader.HtmlDownloader()
        #声明解析器对象
        self.parser = html_parser.HtmlParser()
        #声明输出器对象
        self.outputer = html_outputer.HtmlOutputer()

    #爬虫主程序
    def craw(self, root_url):
        #对网址数量计数
        count = 1
        #将起始搜索页面的url添加进管理器
        self.urls.add_new_url(root_url)
        #如果有新的url存在
        while self.urls.has_new_url():
            #try...catch 用来捕获异常
            try:
                #获取url
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                #下载html文件
                html_cont = self.downloader.download(new_url)
                #解析html文件
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                #添加新的url
                self.urls.add_new_urls(new_urls)
                #传递满足要求的数据
                self.outputer.collect_data(new_data)

                #限制爬取页面的数量
                if count == 100:
                    break
                count = count + 1
            except:
                print 'craw failed'
        #输出需要的信息到html文件
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    #声明主类对象
    obj_spider = SpiderMain()
    #调用爬虫函数
    obj_spider.craw(root_url)