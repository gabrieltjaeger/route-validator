class RouteParserService:
    def __init__(self, country):
        self.country = country

    def parse_route(self, route):
        state_abbreviations = route.split(',')
        states = [self.country.get_state(abbr) for abbr in state_abbreviations]
        if not all(states):
            raise ValueError("Invalid state abbreviation in route")
        return states
