from models.profile import Profile
from models.vip_profile import VipProfile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Apply/Remove Vip Status on Profile")
    print("---------------------------------------------------------------")

    i = 1
    for profile in Profile.objects:
        print('{} - {}'.format(i, profile.get_name()))
        i += 1

    try:
        profile_id = int(input("Type the profile id you want to change status: "))
        profile = Profile.objects[profile_id-1]

        if(type(profile)==Profile):
            new_profile = VipProfile(profile.get_name())
        else:
            new_profile = Profile(profile.get_name())

        new_profile.set_likes(profile.get_likes())
        new_profile.save()
        profile.delete()

    except:
        traceback.print_exc()
    
