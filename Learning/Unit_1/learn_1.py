        #================================================================
# 网络爬虫简介
#----------------------------------------------------------------

#----------------------------------------------------------------


#========识别网站所用的技术========================================================
# pip install builtwith
#----------------------------------------------------------------
# import builtwith
# # url = 'http://example.webscraping.com'
# url = 'http://civil.seu.edu.cn/'
# a = builtwith.parse(url)
# print(a)
#----------------------------------------------------------------


#========寻找网站的所有者========================================================
# 使用WHOIS协议查询域名的注册者
# pip install python-whois
#----------------------------------------------------------------
# import whois
# print(whois.whois('appspot.com'))
# print(whois.whois('www.buseu.cn'))
#----------------------------------------------------------------


#=======下载网页=========================================================
# 确保发生5xx错误时 重新下载
# 设置用户代理
#----------------------------------------------------------------
import urllib.request

def download(url, num_retries=2):
	print('Downloading:',url)
	try:
		#写入User Agent信息
		head = {}
		head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
 		#创建Request对象
		req = urllib.request.Request(url, headers=head)
    	#传入创建好的Request对象
		response = urllib.request.urlopen(req)
		html = response.read().decode('UTF-8')
	except urllib.request.URLError as e:
		print('Download error:',e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e,'code') and 500<=e.code<600:
				# recursively retry 5xx HTTP errors
				return download(url, num_retries-1)
	return html

# url = 'http://www.buseu.cn/'
# # url = 'http://httpstat.us/500'
# # url = 'http://www.meetup.com/'
# html = download(url)
# print(html)
#----------------------------------------------------------------


#========网站地图爬虫========================================================
# robots.txt 从<loc>标签中提取出URL
#----------------------------------------------------------------
# import re

# def crawl_sitemap(url):
# 	# download the sitemap file	
# 	sitemap = download(url)
# 	# extract the sitemap links
# 	links = re.findall('<loc>(.*?)</loc>',sitemap)
# 	# download each link
# 	for link in links:
# 		html = download(link)
# 		# scrape html here ...

# crawl_sitemap('http://example.webscraping.com/robots.txt')
#----------------------------------------------------------------


#========ID遍历爬虫========================================================
# http://example.webscraping.com/places/default/view/Afghanistan-1
# http://example.webscraping.com/places/default/view/Aland-Islands-2
# http://example.webscraping.com/places/default/view/Albania-3
# 忽略网站别名 直接遍历ID
# http://example.webscraping.com/places/default/view/1
# http://example.webscraping.com/places/default/view/2
# http://example.webscraping.com/places/default/view/3 
#----------------------------------------------------------------
# import itertools

# for page in itertools.count(1):
# 	url = 'http://example.webscraping.com/places/default/view/-%d' % page
# 	html = download(url)
# 	if html is None:
# 		break
# 	else:
# 		# success can scrape the result
# 		pass
# # 存在问题 若访问有某个间隔点 爬虫就会立即退出 
# # 下为改进版本 连续发生多次下载错误后 才会退出

# # maximum number of consecutive download errors allowed
# max_errors = 5
# # current number of consecutive download errors
# num_errors = 0
# for page in itertools.count(1):
# 	url = 'http://example.webscraping.com/places/default/view/-%d' % page
# 	html = download(url)
# 	if html is None:
# 		# received an error trying to download this webpage
# 		num_errors += 1
# 		if num_errors == max_errors:
# 			break
# 		else:
# 			num_errors = 0
#----------------------------------------------------------------


#========链接爬虫========================================================
# 用正则表达式来确定需要下载哪些页面
# 使用urlparse模块创建绝对路径
# 记录哪些已经被爬取过 避免重复下载

# 要爬取的是国家列表索引页和国家页面
# http://example.webscraping.com/index/1
# http://example.webscraping.com/view/Afghanistan-1
#----------------------------------------------------------------

# import re
# import urllib.parse

# def link_crawler(seed_url, link_regex):
# 	"""Crawl from the given seed URL following links matched by link_regex"""
# 	crawl_queue = [seed_url]
# 	# keep track which URL's have seen before
# 	seen = set(crawl_queue) # set()一种集合类型 创建集合set、集合set添加、集合删除、交集、并集、差集
# 	while crawl_queue:
# 		url = crawl_queue.pop() # pop() 移除列表中的一个元素
# 		html = download(url)
# 		# filter for links matching our regular expression
# 		for link in get_links(html):
# 			if re.match(link_regex, link):
# 				link = urllib.parse.urljoin(seed_url, link)
# 				# check if have already seen this link
# 				if link not in seen:
# 					seen.add(link)
# 					crawl_queue.append(link)
# 					print(link)

# def get_links(html):
# 	"""Return a list of links from html"""
# 	# a regular expression to extract all links from the webpages
# 	webpages_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
# 	return webpages_regex.findall(html)

# link_crawler('http://example.webscraping.com','/places/default/(index|view)')
#----------------------------------------------------------------


#========下载限速========================================================
# 两次下载直接添加延迟
#----------------------------------------------------------------
# import datetime
# import time

# class Throttle:
# 	""" Add a delay between downloads to the same domain
# 	"""
# 	def __init__(self,delay):
# 		self.delay = delay
# 		# timestamp of when a domain was last accessed
# 		self.domains = {}

# 	def wait(self, url):
# 		domain = urllib.parse.urlparse(url).netloc
# 		last_accessed = self.domains.get(domain)

# 		if self.delay > 0 and last_accessed is not None:
# 			sleep_secs = self.delay - (datetime.datetime.now()-last_accessed).seconds
# 			if sleep_secs > 0:
# 				time.sleep(sleep_secs)
# 		self.domains[domain] = datetime.datetime.now()

# delay = 10
# throttle = Throttle(delay)
# url = 'http://example.webscraping.com'
# throttle.wait(url)
# result = download(url)
# print(result)
#----------------------------------------------------------------


#================================================================
# 
#----------------------------------------------------------------

#----------------------------------------------------------------


