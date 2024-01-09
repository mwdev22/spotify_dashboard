from ..utils.extenisons import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    spotify = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100))
    display_name = db.Column(db.String(40), nullable=False)
    subscription = db.Column(db.String(12), default='free')  
    followers = db.Column(db.Integer)

    def __init__(self,spotify,email,display_name,subscription,followers):
        self.spotify = spotify
        self.email = email
        self.display_name = display_name
        self.subscription = subscription
        self.followers = followers

    # number of users
    @classmethod
    def count_users(cls):
        return cls.query.count()
    
    @classmethod
    def average_followers(cls):
        total_users = cls.query.count()
        total_followers = db.session.query(db.func.sum(User.followers)).scalar()

        if total_users == 0:
            return 0  

        average_followers = total_followers // total_users
        return average_followers
    
