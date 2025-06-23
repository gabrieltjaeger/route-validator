class ValidateRouteUseCase:
    def __init__(self, route_parser, route_validation_service):
        self.route_parser = route_parser
        self.route_validation_service = route_validation_service

    def execute(self, route):
        route = self.route_parser.parse_route(route)
        if not route:
            return False
        return self.route_validation_service.validate_route(route)