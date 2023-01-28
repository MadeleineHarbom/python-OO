from random import choices
import string


class Password:
    INPUT_UNIVERSE = {
        "letters": list(string.ascii_letters),
        "numbers": list(string.digits),
        "punctuations": list(string.punctuation),
    }

    def __init__(self, strength='mid', length=12):
        self.strength = strength
        self.length = length
        self.password = self._generate_password()

    def show_input_universe(self):
        return self.INPUT_UNIVERSE

    def _generate_password(self):
        if self.strength == 'low':
            options = self.INPUT_UNIVERSE['letters']
        elif self.strength == 'mid':
            options = self.INPUT_UNIVERSE['letters'] + self.INPUT_UNIVERSE['numbers']
        elif self.strength == 'high':
            options = self.INPUT_UNIVERSE['letters'] + self.INPUT_UNIVERSE['numbers'] + self.INPUT_UNIVERSE[
                'punctuations']
        else:
            raise TypeError
        password = "".join(choices(options, k=self.length))
        return password


if __name__ == "__main__":
    pw = Password()
    print(pw.password)
