from models.profile import Profile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Like a Profile")
    print("---------------------------------------------------------------")

    i = 1
    for profile in Profile.objects:
        print('{} - {}'.format(i, profile.name))
        i += 1

    try:
        profile_id = int(input("Type the profile id you want to like: "))
        profile = Profile.objects[profile_id-1]

        print('Liking profile: {} - {}'.format(profile_id, profile.name))
        profile.like()
    except:
        print('Type a valid profile id!')

