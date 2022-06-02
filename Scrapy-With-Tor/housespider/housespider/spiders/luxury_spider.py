import scrapy
from scrapy import Request
from csv import DictWriter

STARTING_PAGE = 1

class LuxurySpider(scrapy.Spider):
    
    # handle_httpstatus_list = [404]
    
    name = 'luxuryestate_spider'
    
    start_urls = [
        'https://www.luxuryestate.com/united-arab-emirates/dubai/dubai?'
    ]
    
    allowed_domains =  [
        'luxuryestate.com'
        ]
    
    # being gentle on the server 
    settings = {
        'DOWNLOAD_DELAY': 4,
        'AUTOTHROTTLE_ENABLED': True,
        'HTTPCACHE_ENABLED': False,
    }
    
    # total pages
    tot_pages = 150
    
    # init constructor
    def __init__(self):
        
        try:
            with open('luxury_properties.csv', 'w') as f:
                # writing columns name
                f.write('Name,Price,Area,Bedrooms,Description,Energy_rating,Agency\n')
        except OSError as e:
            print(f'File already existing {e}')
    
    # spider's entry point
    def start_request(self):
        # sending HTTP request
        for url in self.start_urls:
            yield Request(
                url=url,
                callback=self.is_tor_and_privoxy_used
            )
            # check if Tor has changed IP
            # yield scrapy.Request(
            #     url='http://icanhazip.com/',
            #     callback=self.is_tor_and_privoxy_used
            # ) 
            
    def parse(self, response):

        print('\n\nSpider: Start')
        print('Is proxy in response.meta?: ', response.meta)
        print("user_agent is: ",response.request.headers['User-Agent'])
        print('\n\n Spider: End')
        
        # avoiding 'next page' technique -> performances enhanced
        try:
            if STARTING_PAGE == 1 and self.start_urls[0]:
                # start from page 2 untill final page
                for page in range(2, self.tot_pages+1):
                    next_page = self.start_urls[0] + 'pag=' + str(page)
                    yield response.follow(url=next_page, callback=self.parse)
        except:
            self.tot_pages = STARTING_PAGE
        
        self.logger.info('Parse function called on %s', response.url)
        print('\n*****PARSING*****\n')
        
        property_links = response.xpath("//a[@class='js_clickable']/@href").getall()
        
        # list of property links
        links = [
            link for link in property_links
        ]
        
        # loop over the property links and send HTTP request
        for url in links:
            yield Request(
                    url=url,
                    callback=self.parse_details
                    )
		
    def is_tor_and_privoxy_used(self, response):
        
        self.logger.info(f'IP: {str(response.body)}')
        print('\n\nSpider: Start')
        print("Is proxy in response.meta?: ", response.meta)  # not header dispo
        print('\n\nSpider: End')

    def parse_details(self, response):
        
        try:
            features = {
                
            'Name': response.xpath(".//h1[@class='serif-light title-property']/text()").get(),
            
            'Price': response.xpath(".//div[@class='text-right price']/text()").get()
            .replace('\n', '€').strip(),
            
            'Area': response.xpath(".//span[@dir='ltr']/text()").get().strip(),
            
            'Bedrooms':  response.xpath(".//div[@class='single-value']/text()").get()
            .strip().replace('\n', ''),
            
            'Description': response.xpath(".//span[@data-role='description-text-content']").get()
            .replace('<span data-role="description-text-content">\n', '').replace('<br>', '')
            .replace('\n', '').strip(),
            
            'Energy Rating': response.xpath(".//div[@class='item-inner short-item feat-item'][9]/div//text()").get().
                strip().replace('\n', ''),
            
            'Agency': response.xpath("//div[@class='agency__name-container']/a/@href").get(),
            }
            
        except:
            features = {
                
                'Name':response.xpath(".//h1[@class='serif-light title-property']/text()").get()
                .strip(),
                
                'Price': 'Price in application',
                
                'Area': response.xpath(".//span[@dir='ltr']/text()").get().strip(),
                
                'Bedrooms':  response.xpath(".//div[@class='single-value']/text()").get()
                .strip().replace('\n', ''),
                
                'Description': response.xpath(".//span[@data-role='description-text-content']").get()
                .replace('<span data-role="description-text-content">\n', '').replace('<br>', '')
                .replace('\n', '').strip(),
                
                'Energy Rating': 'Missing',
                
                'Agency': response.xpath("//div[@class='agency__name-container']/a/@href").get(),
        }
        
        # write the data into the csv file           
        with open('luxury_properties.csv', 'a') as f:
                csv_writer = DictWriter(f, fieldnames=features.keys())
                csv_writer.writerow(features) 
    