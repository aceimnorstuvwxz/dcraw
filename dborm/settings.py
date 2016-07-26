#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
(C) 2016 Unicall

Description: Database ORM connections

Author: chenbingfeng
'''

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


''' database config'''
engine = create_engine('mysql+mysqldb://root:@localhost/unc_spider_results', echo=True)

''' ORM mapping declaration'''
Base = declarative_base()

class CompanyInfo(Base):
    __tablename__ = 'company_info'
    company_id = Column(Integer, primary_key=True)
    company_name = Column(String)
    company_description = Column(String)
    
    def __repr__(self):
        return "<CompanyInfo(company_id='%s', company_name='%s', company_description='%s')>" % (self.company_id, self.company_name, self.company_description)
        
class UrlHashInfo(Base):
    __tablename__ = "UrlHashInfo"
    urlhash = Column(String, primary_key=True)

    def __repr__(self):
        return "<urlhash(urlhash='%s')>" % (self.urlhash)


Session = sessionmaker(bind=engine)

''' local test
print CompanyInfo.__table__
comp = CompanyInfo(company_name="sdfs", company_description="dfds")
print comp.company_name
session = Session()
session.add(comp)
'''

''' exported APIs '''
def push_CompanyItem(item):
    com = CompanyInfo(company_name=item['name'], company_description=item['description'])
    session = Session()
    session.add(com)
    session.commit()
    
def isexist_CompanyItem(item):
    session = Session()
    cnt = session.query(CompanyInfo).filter(CompanyInfo.company_name == item['name']).count()
    session.commit()
    if cnt > 0:
        return True
    else:
        return False
    
def push_url(md5url):
    if isexist_url(md5url):
        pass
    else:
        com = UrlHashInfo(urlhash=md5url)
        session = Session()
        session.add(com)
        session.commit()

def isexist_url(md5url):
    session = Session()
    cnt = session.query(UrlHashInfo).filter(UrlHashInfo.urlhash == md5url).count()
    session.commit()
    if cnt > 0:
        return True
    else:
        return False
    