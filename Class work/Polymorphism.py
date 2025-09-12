#Polymorphism

class Youtube:
    def playvideo(self):
        print("Video is running with....")
        print("Ads will run")
        print("No background play")
        print("Low quality available")
        print("Play back speed (upto 2x)")

    def youtubeMusic(self):
        print("No access to YouTube Music in free version")

    def likes(self):
        print("You can like videos")

    def share(self):
        print("You can share videos with others")

    def comments(self):
        print("You can comment on videos")

    def subscribe(self):
        print("You can subscribe to channels")

    def upload(self):
        print("You can upload your own videos")

    def watchhistory(self):
        print("You can view your watch history")

    def downloads(self):
        print("No access to Downloads in free version")

class YoutubePremium(Youtube):
    def playvideo(self):
        print("Video is running with....")
        print("No ads")
        print("Background play available")
        print("High quality ")
        print("Play back speed (upto 2x)")

    def youtubeMusic(self):
        print("Access granted to YouTube Music")

    def downloads(self):
        print("Videos can be downloade all videos with high quality")

Revathi=YoutubePremium()
print("\nRevathi-YoutubePremium")
Revathi.playvideo()
Revathi.youtubeMusic()
Revathi.likes()
Revathi.share()
Revathi.comments()
Revathi.subscribe()
Revathi.upload()
Revathi.watchhistory()
Revathi.downloads()
Sony=Youtube()
print("\nSony-Normal User")
Sony.playvideo()
Sony.youtubeMusic()
Sony.likes()
Sony.share()
Sony.comments()
Sony.subscribe()
Sony.upload()
Sony.watchhistory()
Sony.downloads()

#Output:

'''Revathi-YoutubePremium
Video is running with....
No ads 
Background play available
High quality
Play back speed (upto 2x)
Access granted to YouTube Music
You can like videos
You can share videos with others
You can comment on videos
You can subscribe to channels
You can upload your own videos
You can view your watch history
Videos can be downloade all videos with high quality

Sony-Normal User
Video is running with....
Ads will run
No background play
Low quality available
Play back speed (upto 2x)
No access to YouTube Music in free version
You can like videos
You can share videos with others
You can comment on videos
You can subscribe to channels
You can upload your own videos
You can view your watch history
No access to Downloads in free version
'''
