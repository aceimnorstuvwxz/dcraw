from scrapy.exceptions import DropItem
from dirbot.items import *
from dborm.settings import push_CompanyItem
from dborm.settings import isexist_CompanyItem


'''
class DBStorePipeline(object):
     
    def process_item(self, item, spider):
        if type(item) is CompanyItem:
            push_CompanyItem(item)
            

class RemoveDuplicatePipeline(object):
    
    def process_item(self, item, spider):
        if type(item) is CompanyItem:
            if isexist_CompanyItem(item):
                raise DropItem("Duplicate company name: %s" % item['name'])
            else:
                return item
'''

class SaveTextPipeline(object):
    
    def process_item(self, item, spider):
        if type(item) is TextItem:
            with  open("textout.txt", "a") as f:
                f.write(item['text']+'\n')

        if type(item) is Text2Item:
            with  open("text2out.txt", "a") as f:
                f.write(item['text']+'\n')



''' local test
class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['description']).lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item
'''



            
        