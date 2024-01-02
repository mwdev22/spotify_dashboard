from ..utils.extenisons import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spotify_id = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100))
    display_name = db.Column(db.String(40), nullable=False)
    subscription = db.Column(db.String(12), default='free')  
    followers = db.Column(db.Integer)


    # number of users
    @staticmethod
    def count_users():
        return User.query.count()
    
    @staticmethod
    def average_followers():
        total_users = User.query.count()
        total_followers = db.session.query(db.func.sum(User.followers)).scalar()

        if total_users == 0:
            return 0  

        average_followers = total_followers // total_users
        return average_followers
    
'''
'display_name': 'maciek wojdyna', 'external_urls': {'spotify': 'https://open.spotify.com/user/21lyrpw25xvrgdxnq25q33hky'}, 'href': 'https://api.spotify.com/v1/users/21lyrpw25xvrgdxnq25q33hky', 'id': '21lyrpw25xvrgdxnq25q33hky', 'images': [{'url': 'https://i.scdn.co/image/ab67757000003b82e52ae25ffe35814cbfcbd08d', 'height': 64, 'width': 64}, {'url': 'https://i.scdn.co/image/ab6775700000ee85e52ae25ffe35814cbfcbd08d', 'height': 300, 'width': 300}], 'type': 'user', 'uri': 'spotify:user:21lyrpw25xvrgdxnq25q33hky', 'followers': {'href': None, 'total': 53}, 'country': 'PL', 'product': 'premium', 'explicit_content': {'filter_enabled': False, 'filter_locked': False}, 'email': 'wojdynam@wit.edu.pl'}
'''