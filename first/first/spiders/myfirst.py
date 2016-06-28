import scrapy
from urlparse import *
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from first.Render import *

from lxml.html import soupparser, fromstring
import lxml.etree
import lxml.html

class Myfirst(CrawlSpider):
	name = 'myfirst'
	SIMILAR_SET= set([])
	# allowed_domains = ['sec.hdu.edu.cn']
	start_urls = ['http://192.168.10.1:8080/']
	rules = [ Rule(LinkExtractor(attrs=['href'] ),follow="true",process_links='clean_link',process_request='clean_request',callback='my_parse')]# get link
	def clean_link(self,links):
		_links = []
		for link in links:
			t = self._format(link.url)
			if t not in self.SIMILAR_SET:
				self.SIMILAR_SET.add(t)
				_links.append(link)
		return _links
	def parse_start_url(self, response):
		orig_url = response.url
		body = response.body
		parse_url = urlparse(orig_url)
		try:
			doc = lxml.html.fromstring(body, base_url=orig_url)
		except lxml.etree.ParserError:
			self.log('ParserError from lxml on %s' % orig_url)
			return
		except lxml.etree.XMLSyntaxError:
			self.log('XMLSyntaxError from lxml on %s' % orig_url)
			return
		forms = doc.xpath('//form')
		if forms:
			self.collect_form_url(forms,orig_url)
		return None
	def collect_form_url(self,forms,orig_url):
		# defalt
		defalt_method = "GET"
		defalt_action = orig_url
		defalt_allow_element = ['InputElement', 'TextareaElement','SelectElement']

		# prase form
		for form in forms: #each form
			if form.method:
				method = form.method
			else:
				method = defalt_method
			if form.action: 
				action = form.action
			else:
				action = defalt_action

			for ip in form.inputs:
				if ip.name and type(ip).__name__ in defalt_allow_element: 
					if type(ip).__name__  == "InputElement":
						print ip.type,ip.name,ip.value


	def _format(self,url):
		if urlparse.urlparse(url)[2] == '':
			url = url+'/'
		url_struct = urlparse.urlparse(url)
		netloc = url_struct[1]
		path = url_struct[2]
		query = url_struct[4]
		
		temp = (netloc,tuple([len(i) for i in path.split('/')]),tuple(sorted([i.split('=')[0] for i in query.split('&')])))
		return temp

	def clean_request(self,r):
		return r

	def my_parse(self,respose):

		orig_url = respose.url
		parse_url = urlparse(parse_url)
		try:
			doc = lxml.html.fromstring(body, base_url=orig_url)
		except lxml.etree.ParserError:
			self.log('ParserError from lxml on %s' % orig_url)
			return
		except lxml.etree.XMLSyntaxError:
			self.log('XMLSyntaxError from lxml on %s' % orig_url)
			return
		forms = doc.xpath('//form')
		if forms:
			print forms