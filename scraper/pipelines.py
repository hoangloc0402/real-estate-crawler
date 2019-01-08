import os

class ScraperPipeline(object):
	def __init__(self):
        # self.collection = connect_db("crawler")["news"]
		self.count = 0
		self.ROOT_DIRECTORY = "/home/cpu10133-local/Projects/Data/bds/"

	def process_item(self, item, spider):
		# self.collection.insert_one(item)
		current_directory = self.ROOT_DIRECTORY + item['domain']
		if not os.path.exists(current_directory):
			os.makedirs(current_directory)
		filename = str(self.count) + '.txt'
		self.count = self.count + 1  
		savepath = current_directory + "/" + filename
		f = open(savepath,"wb")
		# print("SAVE FILE::::::::::: ", filename)
		f.write(str(item).encode("utf-8"))
		f.close() 
		return item

    # def connect_db(db_name):
    #     return MongoClient("mongodb://localhost:27017")[db_name]