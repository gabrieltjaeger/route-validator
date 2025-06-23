class State:
    def __init__(self, name, abbreviation, neighbors):
        self.name = name
        self.abbreviation = abbreviation
        self.neighbors = neighbors
        
    def is_neighbor(self, state_abbreviation):
        return state_abbreviation in self.neighbors