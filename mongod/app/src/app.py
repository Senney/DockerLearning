import os
from faker import Faker
import pymongo


if __name__ == '__main__':
    mongo_connection = os.environ['MONGO_PORT'].\
        replace('tcp://', 'mongodb://')

    client = pymongo.MongoClient(mongo_connection)
    db = client.appdb

    faker = Faker()
    for i in range(0, 10):
        user_profile = faker.profile()
        result = db.users.insert_one({
            'userid': user_profile['username'],
            'password': 'Password!',
            'email': user_profile['mail'],
            'pii': {
                'dob': user_profile['birthdate'],
                'full_name': user_profile['name'],
                'sex': user_profile['sex']
            }
        })

        print('Added id: {}'.format(result.inserted_id))

    cursor = db.users.find().sort([
        ('userid', pymongo.DESCENDING)
    ])
    for user in cursor:
        print('User ID: {}'.format(user['userid']))
