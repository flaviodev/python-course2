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
            print('{} - {}'.format(i, profile.to_string()))
            i += 1

    except Exception as e: print(e)
