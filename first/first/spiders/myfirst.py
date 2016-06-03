import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class Myfirst(CrawlSpider):
	name = 'myfirst'
	allowed_domains = ['sec.hdu.edu.cn']
	start_urls = ['http://sec.hdu.edu.cn/']
	rules = ( Rule(LinkExtractor( ),follow="true",callback='my_parse'),)

	def my_parse(self,respose):
		# return scrapy.FormRequest.from_response(respose,formdata={'user': 'john', 'pass': 'secret'},callback='my_parse')
		with open('1.txt','a') as f:
			f.write(respose.url+'\n')
	# def my_parse(self,respose):
	# 	return respose.url