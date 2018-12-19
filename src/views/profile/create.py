from models.profile import Profile
from models.vip_profile import VipProfile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Create a new Profile")
    print("---------------------------------------------------------------")

    profile_vip = input("Is the profile vip? (y/n) ")
    profile_name = input("Type the profile name: ")

    if(profile_vip == 'y' or profile_vip == 'Y'):
        profile = VipProfile(profile_name)
    else: 
        profile = Profile(profile_name)

    profile.save()
    
