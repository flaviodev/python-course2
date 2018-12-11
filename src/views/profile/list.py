from models.profile import Profile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Profiles")
    print("---------------------------------------------------------------")

    

    i = 1
    for profile in Profile.objects:
        print('{} - {} ({} likes)'.format(i, profile.name, profile.get_likes() if not None else 0))
        i += 1

