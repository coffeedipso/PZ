tours = {
    "Voyage": {"Mexico", "Canada", "Israel", "Italy", "USA"},
    "ReynaTour": {"England", "Japan", "Canada", "South Africa"},
    "Rainbow": {"USA", "Spain", "Sweden", "Australia"}
}

def find_tour_agencies(country):
    agencies = []
    for agency, countries in tours.items():
        if country in countries:
            agencies.append(agency)
    return agencies

def find_tour_agencies_exclude(country):
    agencies = []
    for agency, countries in tours.items():
        if country not in countries:
            agencies.append(agency)
    return agencies

def find_all_tours():
    all_tours = set()
    for countries in tours.values():
        all_tours.update(countries)
    return all_tours

try:
    japan_agencies = find_tour_agencies("Japan")
    print("Туры в Японию можно приобрести в следующих турагентствах:", japan_agencies)

    sa_agencies = find_tour_agencies_exclude("South Africa")
    if sa_agencies:
        print("Туры в ЮАР нельзя приобрести в следующих турагентствах:", sa_agencies)
    else:
        print("Туры в ЮАР можно приобрести во всех турагентствах")

    all_tours = find_all_tours()
    print("Полный список туров:", all_tours)

except Exception as e:
    print("Произошла ошибка:", e)
