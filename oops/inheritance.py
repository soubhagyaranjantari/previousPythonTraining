class insta1:
    def __init__(self):
        self.insta_version=1
    def uploadpic(self):
            print('upload ur pic')
    def upload_multiplepic(self):
            print('upload ur multiple pic')    

class insta2(insta1):
    def __init__(self):
        self.insta_version=2
    def reels(self):
        print('play reels')
    def group_call(self):
        print('make a group call')
    
class insta3(insta2):
    def __init__(self):
        self.insta_version=3
    def filter(self):
        print('use filter')
    def watch_togather(self):
        print('watch togather with ur friends')

o3=insta3()
o3.upload_multiplepic()
o3.reels()
print(o3.insta_version)