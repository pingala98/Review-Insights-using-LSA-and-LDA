# -*- coding: utf-8 -*-
 
# Importing Scrapy Library
import scrapy
 
# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
     
    # Spider name
    name = 'amazon_reviews'
     
    # Domain names to scrape
    allowed_domains = ['amazon.in']
     
    # Base URL 
   
    myBaseUrl = "https://www.amazon.in/Redmi-Note-Pro-Electric-Processor/product-reviews/B07X2KLYSF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber="
    start_urls=[]
    
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,720):
        start_urls.append(myBaseUrl+str(i))
    
    # Defining a Scrapy parser
    def parse(self, response):
            #Get the Review List
            data = response.css('#cm_cr-review_list')
            
            #Get the Name
            name = data.css('.a-profile-name')
            
            #Get the Review Title
            title = data.css('.review-title')
            
            # Get the Ratings
            star_rating = data.css('.review-rating')
            
            # Get the users Comments
            comments = data.css('.review-text')
            count = 0
             
            # combining the results
            for review in star_rating:
                yield{'Name':''.join(name[count].xpath(".//text()").extract()),
                      'Title':(''.join(title[count].xpath(".//text()").extract())).strip(),
                      'Rating': ''.join(review.xpath('.//text()').extract()),
                      'Comment': (''.join(comments[count].xpath(".//text()").extract())).strip()
                     }
                count=count+1
