from models.profile import Profile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Delete a Profile")
    print("---------------------------------------------------------------")

    i = 1
    for profile in Profile.objects:
        print('{} - {}'.format(i, profile.name))
        i += 1

    try:
        profile_id = int(input("Type the profile id you want to delete: "))
        profile = Profile.objects[profile_id-1]

        print('Deleting profile: {} - {}'.format(profile_id, profile.name))
        profile.delete()
    except:
        print('Type a valid profile id!')

