BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

ITEM_PIPELINES = {'scraper.pipelines.ScraperPipeline': 1}

ROBOTSTXT_OBEY = True

