__author__ = 'Mohnish'

import pymongo

uri = 'mongodb://127.0.0.1:27017'
client = pymongo.MongoClient(uri)

database = client['test']
collection = database['students']

#students = collection.find({})
students = [student for student in collection.find({})]
#print(students)


students_mark = [item['marks'] for item in collection.find({}) if item['marks'] == 90]
print(students_mark)