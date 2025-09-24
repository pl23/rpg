class text_UI:

    def __init__(self, options_string=[], options_funk=[]):
        self.options_string = options_string
        self.options_funk = options_funk
        self.options = []

    def update(self, options_string=[], options_funk=[]):
        if options_funk != []:
            self.options_funk = options_funk

        if options_string != []:
            self.options_string = options_string

    def UI_input(self):
        try:
            user_input = int(input("Enter your choice: "))
            if 1 <= user_input <= len(self.options_string):
                return user_input - 1
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print("Invalid input. Please enter a number.")
            print(e)

    def UI_selection_options(self):
        print("Please select an option:")
        for i, option in enumerate(self.options_string):
            print(f"{i + 1}. {option}")
        self.UI_input()

    def execute_select(self):
        user_input = self.UI_input()
        if user_input is not None:
            return self.options_funk[user_input]()
