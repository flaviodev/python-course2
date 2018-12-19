import traceback
from models.profile import Profile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Update a Profile")
    print("---------------------------------------------------------------")

    i = 1
    for profile in Profile.objects:
        print('{} - {}'.format(i, profile.get_name()))
        i += 1

    try:
        profile_id = int(input("Type the profile id you want to update: "))
        profile = Profile.objects[profile_id-1]
        profile_name = input("Type the profile name: ")
        profile.set_name(profile_name)
        
        profile_vip = input("Is the profile vip? (y/n) ")
        if(profile_vip == 'y' or profile_vip == 'Y'):
            profile.set_vip(True)
        else: 
            profile.set_vip(False)

        profile.save()
    except:
        traceback.print_exc()