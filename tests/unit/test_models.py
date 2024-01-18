from app.models.users import User

import os

def test_user_model(app):
    with app.app_context():
        # Create a user
        user1 = User(spotify="1r4greg45963856", email="user1@example.com", display_name="User 1", subscription="free", followers=500)
        user2 = User(spotify="dsafsadfvx75647czbd", email="user2@example.com", display_name="User 2", subscription="premium", followers=1000)
        user3 = User(spotify="uiti65787657kfghsghfs", email="user3@example.com", display_name="User 3", subscription="premium", followers=2000)
        user4 = User(spotify="asdfdsavcdsarewqr24523", email="user4@example.com", display_name="User 4", subscription="free", followers=800)

        user1.save()  
        user2.save()  
        user3.save()  
        user4.save()  

        assert User.count_users() == 4

        # Test average_followers method
        assert User.average_followers() == (user1.followers + user2.followers + user4.followers + user3.followers) // User.count_users()  