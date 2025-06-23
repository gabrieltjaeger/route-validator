class Country:
    def __init__(self, name, abbreviation, states):
        self.name = name
        self.abbreviation = abbreviation
        self.states = states

    def get_state(self, abbreviation):
        return self.states.get(abbreviation)