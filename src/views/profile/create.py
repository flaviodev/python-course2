from models.profile import Profile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Create a new Profile")
    print("---------------------------------------------------------------")

    profile_name = input("Type the profile name: ")
    profile = Profile(profile_name)

    profile_vip = input("Is the profile vip? (y/n) ")
    if(profile_vip == 'y' or profile_vip == 'Y'):
        profile.set_vip(True)
    else: 
        profile.set_vip(False)

    profile.save()
    
