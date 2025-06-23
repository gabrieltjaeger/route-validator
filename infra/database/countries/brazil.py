from core.entities.country import Country
from core.entities.state import State

BRAZIL = Country("Brasil", "BR", {
      "AC": State("Acre", "AC", ["AM", "RO"]),
      "AL": State("Alagoas", "AL", ["PE", "SE", "BA"]),
      "AP": State("Amapá", "AP", ["PA"]),
      "AM": State("Amazonas", "AM", ["RO", "PA", "MT", "RR", "AC"]),
      "BA": State("Bahia", "BA", ["SE", "AL", "PE", "PI", "TO", "GO", "MG", "ES"]),
      "CE": State("Ceará", "CE", ["RN", "PB", "PE", "PI"]),
      "DF": State("Distrito Federal", "DF", ["GO", "MG"]),
      "ES": State("Espírito Santo", "ES", ["BA", "MG", "RJ"]),
      "GO": State("Goiás", "GO", ["DF", "MG", "TO", "BA", "MT", "MS"]),
      "MA": State("Maranhão", "MA", ["PI", "TO", "PA"]),
      "MT": State("Mato Grosso", "MT", ["RO", "AM", "PA", "TO", "GO", "MS"]),
      "MS": State("Mato Grosso do Sul", "MS", ["PR", "SP", "MG", "GO", "MT"]),
      "MG": State("Minas Gerais", "MG", ["ES", "RJ", "SP", "MS", "GO", "DF", "BA"]),
      "PA": State("Pará", "PA", ["AP", "RR", "AM", "MT", "TO", "MA"]),
      "PB": State("Paraíba", "PB", ["PE", "RN", "CE"]),
      "PE": State("Pernambuco", "PE", ["PB", "CE", "PI", "BA", "AL"]),
      "PR": State("Paraná", "PR", [ "SC", "SP", "MS"]),
      "PI": State("Piauí", "PI", ["BA", "PE", "CE", "MA", "TO"]),
      "RJ": State("Rio de Janeiro", "RJ", ["SP", "MG", "ES"]),
      "RN": State("Rio Grande do Norte", "RN", ["CE", "PB"]),
      "RS": State("Rio Grande do Sul", "RS", ["SC"]),
      "RO": State("Rondônia", "RO", ["AC", "AM", "MT"]),
      "RR": State("Roraima", "RR", ["AM", "PA"]),
      "SC": State("Santa Catarina", "SC", ["RS", "PR"]),
      "SP": State("São Paulo", "SP", ["PR", "MS", "RJ", "MG"]),
      "SE": State("Sergipe", "SE", ["AL", "BA"]),
      "TO": State("Tocantins", "TO", ["BA", "PI", "MA", "PA", "MT", "GO"])      
    })