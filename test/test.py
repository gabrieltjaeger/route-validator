import pytest

from core.entities.country import Country
from core.entities.state import State
from core.use_cases.validate_route_use_case import ValidateRouteUseCase
from infra.services.route_parser_service import RouteParserService
from infra.services.route_validation_service import RouteValidationService


@pytest.fixture
def brazil():
    return Country("Brasil", "BR", {
        "MG": State("Minas Gerais", "MG", ["GO", "DF"]),
        "GO": State("Goiás", "GO", ["DF", "MG", "TO"]),
        "DF": State("Distrito Federal", "DF", ["GO", "MG"]),
        "TO": State("Tocantins", "TO", ["GO"]),
        "SP": State("São Paulo", "SP", ["MG"]),
    })

@pytest.fixture
def route_parser(brazil):
    return RouteParserService(brazil)

@pytest.fixture
def route_validation_service():
    return RouteValidationService()

@pytest.fixture
def validate_route_use_case(route_parser, route_validation_service):
    return ValidateRouteUseCase(route_parser, route_validation_service)


def test_state_is_neighbor():
    mg = State("Minas Gerais", "MG", ["GO", "DF"])
    assert mg.is_neighbor("GO")
    assert mg.is_neighbor("DF")
    assert not mg.is_neighbor("SP")

def test_country_get_state(brazil):
    assert brazil.get_state("MG").name == "Minas Gerais"
    assert brazil.get_state("SP").abbreviation == "SP"
    assert brazil.get_state("XX") is None

def test_route_parser_valid_route(route_parser):
    route = "MG,GO,DF"
    states = route_parser.parse_route(route)
    assert [s.abbreviation for s in states] == ["MG", "GO", "DF"]

def test_route_parser_invalid_route(route_parser):
    with pytest.raises(ValueError):
        route_parser.parse_route("MG,XX,DF")

def test_route_validation_service_valid(route_validation_service, brazil):
    mg = brazil.get_state("MG")
    go = brazil.get_state("GO")
    df = brazil.get_state("DF")
    assert route_validation_service.validate_route([mg, go, df]) is True

def test_route_validation_service_invalid(route_validation_service, brazil):
    mg = brazil.get_state("MG")
    sp = brazil.get_state("SP")
    to = brazil.get_state("TO")
    assert route_validation_service.validate_route([mg, sp, to]) is False

def test_route_validation_service_too_short(route_validation_service, brazil):
    mg = brazil.get_state("MG")
    assert route_validation_service.validate_route([mg]) is False
    assert route_validation_service.validate_route([]) is False

def test_validate_route_use_case_valid(validate_route_use_case):
    assert validate_route_use_case.execute("MG,GO,DF") is True

def test_validate_route_use_case_invalid(validate_route_use_case):
    assert validate_route_use_case.execute("MG,SP,TO") is False

def test_validate_route_use_case_invalid_abbreviation(validate_route_use_case):
    with pytest.raises(ValueError):
        validate_route_use_case.execute("MG,XX,DF")