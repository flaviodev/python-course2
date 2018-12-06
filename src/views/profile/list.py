from models.profile import Profile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Profiles")
    print("---------------------------------------------------------------")

    for profile in Profile.objects:
        print(profile.name)
