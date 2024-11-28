

def test_database(url):
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

def test_resd_write_access():


    ""
    try:
        database = client.get_database("sample_mflix")
        movies = database.get_collection("movies")


        # Query for a movie that has the title 'Back to the Future'
        query = { "title": "The Great Train Robbery" }
        movie = movies.find_one(query)

        client.close()

    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)
    


# with app.app_context():
#     user = User(username='JohnDoe', wallet_address='0x1244444')
#     db.session.add(user)
#     db.session.commit()
#     print("=============================")