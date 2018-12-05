import views.profile.create
import app.menu

if(__name__ == "__main__"):
    run()

def run():
    options = {1 : "Create Profile"}
    functions = {1 : views.profile.create }

    app.menu.show_menu('Profiles', options, functions )

