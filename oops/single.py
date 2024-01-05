class user_id:
    def __init__(self,name,userid):
        self.name=name
        self.userid=userid
    def get_Details(self):
        print(f'name of the user is {self.name}')
        print(f'id of this user is {self.userid}')

class account(user_id):
    def __init__(self, name, userid):
        super().__init__(name, userid)
        self.profile='imfo of user'
        self.photo='photos of user'
        self.privecy='privecy of user'
    def details_account(self):
        print(f'name of the user is {self.name}\nid of user is{self.userid}\nphotos of user is {self.photo}\nprofile of the user is {self.profile}\nuser detais {self.privecy}')


a=account('Spider man','spider123@any.com')
a.details_account()