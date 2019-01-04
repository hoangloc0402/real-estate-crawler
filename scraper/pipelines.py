

class ScraperPipeline(object):
    # def __init__(self):
    #     self.collection = connect_db("crawler")["news"]
	count = 0

	def process_item(self, item, spider):
		# self.collection.insert_one(item)
		filename = str(self.count) + '.txt'
		self.count = self.count + 1    
		f = open("/home/cpu10133-local/crawled_data/" + filename,"w")
		print("SAVE FILE::::::::::: ", filename)
		f.write(str(item))
		f.close()          
		return item

    # def connect_db(db_name):
    #     return MongoClient("mongodb://localhost:27017")[db_name]