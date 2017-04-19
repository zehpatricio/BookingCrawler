 # -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from bookingcrawler.items import *
from scrapy.http import request

class BookingSpider(Spider):
	name = "booking"
	allowed_domains = ["www.booking.com"]
	start_urls = ["https://www.booking.com/reviews/br/hotel/luzeiros.pt-br.html?r_lang=pt&order=completed_desc&page="+str(i) for i in range(3, 13)]

	def parse(reviewf, response):
		reviews = response.css('.review_item')

		for review in reviews:
			item = BookingcrawlerItem()
			item['date'] = review.css('.review_item_date::text').extract_first().replace("\n", "")
			item['author'] = review.css('.review_item_reviewer>h4>span::text').extract_first()
			item['country'] = review.css('.review_item_reviewer>span.reviewer_country>span>span::text').extract_first()
			item['number_of_avaliations'] = int(review.css('.review_item_reviewer>.review_item_user_review_count::text').extract_first()\
								.replace("\n", "").split(" ")[0])
			item['score'] = float(review.css('.review_item_review_score::text').extract_first().replace("\n", "").replace(",", "."))
			item['title'] = review.css('a.review_item_header_content>span::text').extract_first()
			item['negative'] = review.css('.review_item_review_content>.review_neg>span::text').extract_first()
			item['positive'] = review.css('.review_item_review_content>.review_pos>span::text').extract_first()
			yield item