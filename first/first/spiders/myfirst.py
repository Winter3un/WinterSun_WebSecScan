import scrapy
import urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Myfirst(CrawlSpider):
	name = 'myfirst'
	SIMILAR_SET= set([])
	allowed_domains = ['sec.hdu.edu.cn']
	start_urls = ['http://sec.hdu.edu.cn/']
	rules = [ Rule(LinkExtractor( ),follow="true",process_links='clean_link',process_request='clean_request',callback='my_parse')]# get link
	def clean_link(self,links):
		_links = []
		for link in links:
			t = self._format(link.url)
			if t not in self.SIMILAR_SET:
				self.SIMILAR_SET.add(t)
				with open('2.txt','a') as f:
					f.write(str(self.SIMILAR_SET)+'\n')
				_links.append(link)
		return _links
	def clean_request(self,r):
		return r
	def my_parse(self,respose):
		# return scrapy.FormRequest.from_response(respose,formdata={'user': 'john', 'pass': 'secret'},callback='my_parse')
		# with open('1.txt','a') as f:
		# 	f.write(respose.url+'\n')
		return None
	def _format(self,url):
		if urlparse.urlparse(url)[2] == '':
			url = url+'/'
		url_struct = urlparse.urlparse(url)
		netloc = url_struct[1]
		path = url_struct[2]
		query = url_struct[4]
		
		temp = (netloc,tuple([len(i) for i in path.split('/')]),tuple(sorted([i.split('=')[0] for i in query.split('&')])))
		return temp