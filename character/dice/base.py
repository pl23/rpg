import random


class Dice:

    def roll(self, sides):
        return random.randint(1, sides)
        #returns a random integer between 1 and sides inclusive
        #sides is an integer that represents the number of sides on the die
        #returns an integer that represents the result of the die roll

    def roll_dice(self, dice):
        results = []
        for die in dice:
            results.append(self.roll(die))
        return results
        #dice is a list of integers that represent the number of sides on each die
        #results is a list of integers that represent the results of each die roll
        #results is returned as a list of integers

    def roll_AdvantageDisadvantage(self, times, sides, mod):
        if mod == True:
            return max(self.roll_dice([sides] * times))
        elif mod == False:
            return min(self.roll_dice([sides] * times))
        else:
            raise ValueError("mod must be True or False")

    def parse_rolls(self, roles={}):
        results = []
        # Assuming all lists have the same length, we can get the number of rolls
        num_rolls = len(roles["times"])

        for i in range(num_rolls):
            current_mod = roles["mod"][i]

            # Check if a modifier is present for the current roll
            if current_mod is not None:
                if current_mod is True:
                    results.append(
                        self.roll_AdvantageDisadvantage(
                            roles["times"][i], roles["side"][i], True))
                elif current_mod is False:
                    results.append(
                        self.roll_AdvantageDisadvantage(
                            roles["times"][i], roles["side"][i], False))
            else:
                # If the modifier is None, perform a standard roll
                results.append(
                    self.roll_dice((roles["times"][i], roles["side"][i])))

        return results

    def parse_math(self, results):
        pass  # Implement the logic to parse and evaluate mathematical expressions
        #calls the parse_rolls function to get the results of the dice rolls
        #returns the final result as an integeror, a list of integers
    def string_parse(self, string):
        pass  # Implement the logic to parse the string and extract the necessary information
        #calls the parse_math function to get the final result
        #returns the final result as an integer or a list of integers and flags
