import instaloader
username = input("enter insta username : ")
instaloader.Instaloader().download_profile(username,profile_pic_only=False)