import views.profile.create
import views.profile.list
import app.menu

if(__name__ == "__main__"):
    run()

def run():
    options = {1 : 'List Profiles', 2 : 'Create Profile'}
    functions = {1 : views.profile.list, 2 : views.profile.create}


    app.menu.show_menu('Profiles', options, functions )

