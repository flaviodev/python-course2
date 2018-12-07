import views.profile.create
import views.profile.list
import views.profile.delete
import views.profile.update
import app.menu

if(__name__ == "__main__"):
    run()

def run():
    options = {1 : 'List Profiles', 2 : 'Create Profile', 3 : 'Update Profile', 4 : 'Delete Profile'}
    functions = {1 : views.profile.list, 2 : views.profile.create, 3 : views.profile.update, 4 : views.profile.delete}


    app.menu.show_menu('Profiles', options, functions )

