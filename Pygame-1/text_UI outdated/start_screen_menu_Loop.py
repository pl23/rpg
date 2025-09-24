import base as text_UI


def start():
    running == True
    while running:
        options_string = ["Start", "Options", "Exit"]
        options_funk = [start_game, options, exit_game]
        text_UI.update(options_string, options_funk)
        text_UI.UI_selection_options()