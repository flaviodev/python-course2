from models.profile import Profile
import views.profile.create
import views.profile.list
import views.profile.update
import views.profile.delete
import views.profile.like
import views.profile.apply_rem_vip
import views.profile.import_csv
import app.menu

if(__name__ == "__main__"):
    run()

def run():
    options = {1 : 'List Profiles', 2 : 'Create Profile', 3 : 'Update Profile', 4 : 'Delete Profile', 5 : 'Like Profile', 6 : 'Apply/Remove Vip', 7 : 'Import from CSV'}
    functions = {1 : views.profile.list, 2 : views.profile.create, 3 : views.profile.update, 4 : views.profile.delete, 5 : views.profile.like, 6 : views.profile.apply_rem_vip, 7 : views.profile.import_csv}


    app.menu.show_menu(Profile.menu_name(), options, functions )

