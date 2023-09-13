import unittest,os,sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from model.db import connectDB,DB
from pymongo.mongo_client import MongoClient
import pymongo


class DBTester(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('Run')
        DBName="Users"
        collectionName='myCollection'

        self.dbClass= DB(DBName=DBName,collection=collectionName)
        self.collection = self.dbClass.getCollection()
    
    def testDBConnection(self):
        self.assertEqual(type(connectDB()), MongoClient)

    def testCollection(self):
        res = type(self.dbClass.getCollection())
        self.assertEqual(res,pymongo.collection.Collection)

    # def testaddData(self,data={'title':4}):
    #     print("Add DATA method")
    #     res  = self.collection.insert_one(data)
    #     self.assertEqual(type(res),pymongo.results.InsertOneResult)

    # def testgetOneData(self,idientifier={'title':1}):
    #     print("Getting Data")
    #     res = self.collection.find_one(idientifier)
    #     print(res)
    #     print(type(res),pymongo.cursor.Cursor)

    def testgetData(self,idientifier={'title':1}):
        print("Getting Data")
        res = self.collection.find(idientifier)
        # for data in res:
        #     print(data)
        self.assertEqual(type(res),pymongo.cursor.Cursor)

    def testindex(self,indexIds=['title_1']):
        print("Finding Indexes")
        for indexId in indexIds:
            indexes = self.collection.index_information()
            isUnique = indexes[indexId]['unique']
        self.assertTrue(isUnique)