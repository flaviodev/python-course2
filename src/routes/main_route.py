import routes.profile_route
import app.menu

if(__name__ == "__main__"):
    run()

def run():
    options = {1 : "Profiles"}
    functions = {1 : routes.profile_route }

    app.menu.show_menu('My Social Network', options, functions )

