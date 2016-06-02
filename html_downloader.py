#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import urllib2


class HtmlDownloader(object):

    def download(self, url):
        #如果url为空，返回None
        if url is None:
            return None
        #创建请求对象
        request = urllib2.Request(url)
        #创建应答对象
        response = urllib2.urlopen(request)
        #状态码200表示请求成功
        if response.getcode() != 200:
            return None
        return response.read()