from models.profile import Profile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Profiles")
    print("---------------------------------------------------------------")

    i = 1
    for profile in Profile.objects:
        print('{} - {}'.format(i, profile.name))
        i += 1

