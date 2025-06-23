class RouteValidationService:
    def __init__(self):
        pass

    def validate_route(self, route):
        if not route or len(route) < 2:
            return False
        for i in range(len(route) - 1):
            current_state = route[i]
            next_state = route[i + 1]

            if not current_state.is_neighbor(next_state.abbreviation):
                return False
        return True
