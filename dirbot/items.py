from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    description = Field()
    url = Field()

class TorrentItem(Item):
    url = Field()
    name = Field()
    description = Field()
    size = Field()


class CompanyItem(Item):
    name = Field()
    description = Field()
    '''
    address = Field()
    phone0 = Field()
    phone1 = Field()
    people_num_min = Field()
    people_num_max = Field()
    category = Field()
    data_src = Field()
    '''

class TextItem(Item):
    text = Field()

class Text2Item(Item):
    text = Field()

