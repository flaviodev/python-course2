from models.profile import Profile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Create a new Profile")
    print("---------------------------------------------------------------")

    profile_name = input("Type the profile name: ")
    profile = Profile(profile_name)
    profile.save()
    
