from models.profile import Profile
from models.vip_profile import VipProfile

if(__name__ == "__main__"):
    run()

def run():
    print("---------------------------------------------------------------")
    print("Import Profiles")
    print("---------------------------------------------------------------")

    csv_file_name = input("Type the csv file path: ")

    csv_file = None

    try:
        csv_file = open(csv_file_name,'r')

        while True:
            line = csv_file.readline()
            line = line.rstrip()

            if(not line): break

            values = line.split(';')

            profile_vip = values[0]
            profile_name = values[1]

            if(profile_vip == 'y' or profile_vip == 'Y'):
                profile = VipProfile(profile_name)
            else: 
                profile = Profile(profile_name)

            profile.save()
    
        csv_file.close()
    except (IOError, TypeError, Error) as error:
        print('ErrorError trying to import file %s' % error)
    finally:
        if(csv_file is not None):
            csv_file.close()


    
