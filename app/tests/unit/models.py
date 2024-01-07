from app.models.users import User
from app.utils.extenisons import db

def test_new_user():

    # user creation testing
    user1 = User(spotify_id="1r4greg45963856", email="user1@example.com", display_name="User 1", subscription="free", followers=500)
    user2 = User(spotify_id="dsafsadfvx75647czbd", email="user2@example.com", display_name="User 2", subscription="premium", followers=1000)
    user3 = User(spotify_id="uiti65787657kfghsghfs", email="user3@example.com", display_name="User 3", subscription="premium", followers=2000)
    user4 = User(spotify_id="asdfdsavcdsarewqr24523", email="user4@example.com", display_name="User 4", subscription="free", followers=800)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)

    db.session.commit()

    assert User.query.first(spotify_id='dsafsadfvx75647czbd')

    # testing methods 
    assert User.count_users() == 4  

    assert User.average_followers() == (user1.followers + user2.followers + user4.followers + user3.followers) // User.count_users()  
