 # -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from bookingcrawler.items import *
from scrapy.http import request

class BookingSpider(Spider):
	name = "booking"
	allowed_domains = ["www.booking.com"]
	# start_urls = ["https://www.booking.com/reviews/br/hotel/marina-park.pt-br.html"]
	# start_urls = ["https://www.booking.com/reviews/br/hotel/cris-florianopolis.pt-br.html"]
	# start_urls = ["https://www.booking.com/reviews/br/hotel/tulip-inn-hangar.pt-br.html"]
	# start_urls = ["https://www.booking.com/reviews/br/hotel/luxor-piaui-teresina.pt-br.html"]
	# start_urls = ["https://www.booking.com/reviews/br/hotel/plaza-inn-paineiras.pt-br.html"]
	# start_urls = ["https://www.booking.com/reviews/br/hotel/sheraton-da-bahia.pt-br.html"]
	start_urls = ["https://www.booking.com/reviews/br/hotel/castro.pt-br.html"]

	def parse(reviewf, response):
		dates = response.xpath('//p[contains(@class, "review_item_date")]/text()').extract()
		authors = response.xpath('//span[contains(@itemprop, "name")]/text()').extract()
		number_of_avaliations = response.xpath('//div[contains(@class, "review_item_user_review_count")]/text()').extract()
		titles = response.xpath('//a[contains(@class, "review_item_header_content")]/span[contains(@itemprop, "name")]/text()').extract()
		positives = response.xpath('//p[contains(@class, "review_")]/span[contains(@itemprop, "reviewBody")]/text()').extract()
		negatives = response.xpath('//p[contains(@class, "review_")]/span[contains(@itemprop, "reviewBody")]/text()').extract()

		reviews = []
		for i in range(len(dates)):
			item = BookingcrawlerItem()
			item['date'] = dates[i]
			item['author'] = authors[i]
			item['number_of_avaliations'] = number_of_avaliations[i]
			item['title'] = titles[i]
			item['positive'] = positives[i].encode('utf-8')
			item['negative'] = negatives[i].encode('utf-8')
			reviews.append(item)
			yield item
		print(str(len(dates))+" Itens encontrados.")