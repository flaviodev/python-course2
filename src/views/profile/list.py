from models.profile import Profile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Profiles")
    print("---------------------------------------------------------------")

    try: 

        i = 1
        for profile in Profile.objects:
            print('{} - {} ({} likes - Credits: $ {})'.format(i, profile.get_name(), profile.get_likes() if not None else 0, profile.get_credits() if profile.is_vip() else '0.0'))
            i += 1

    except Exception as e: print(e)
