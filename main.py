from core.use_cases.validate_route_use_case import ValidateRouteUseCase
from infra.database.countries.brazil import BRAZIL
from infra.services.route_parser_service import RouteParserService
from infra.services.route_validation_service import RouteValidationService


def main():
    route_parser = RouteParserService(BRAZIL)
    route_validation_service = RouteValidationService()
    validate_route_use_case = ValidateRouteUseCase(route_parser, route_validation_service)
    
    route = input()
    is_valid = validate_route_use_case.execute(route)
    print(is_valid)

if __name__ == "__main__":
    main()