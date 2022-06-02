import scrapy


class IfconfigSpider(scrapy.Spider):
    name = 'check_ip'
    allowed_domains = ['ifconfig.me']
    start_urls = ['https://ifconfig.me/']

    def parse(self, response, **kwargs):
        user_agent = response.request.headers.get('User-Agent')
        self.log(f'User Agent: {user_agent}')

        ip = response.xpath('//strong[@id="ip_address"]/text()').get()
        self.log(f'IP: {ip}')