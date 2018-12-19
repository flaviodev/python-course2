import views.profile.create
import views.profile.list
import views.profile.update
import views.profile.delete
import views.profile.like
import views.profile.apply_rem_vip
import app.menu

if(__name__ == "__main__"):
    run()

def run():
    options = {1 : 'List Profiles', 2 : 'Create Profile', 3 : 'Update Profile', 4 : 'Delete Profile', 5 : 'Like Profile', 6 : 'Apply/Remove Vip'}
    functions = {1 : views.profile.list, 2 : views.profile.create, 3 : views.profile.update, 4 : views.profile.delete, 5 : views.profile.like, 6 : views.profile.apply_rem_vip}


    app.menu.show_menu('Profiles', options, functions )

