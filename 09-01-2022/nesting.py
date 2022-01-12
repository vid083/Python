
# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg"]
}

# Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visted": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12},
    "Germany": ["Berlin", "Hamburg"]
}

# Nesting Dictionary in a List
travel_log = [
    {
    "country": "France", 
    "cities_visted": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
    },
    { 
    "country": "Germany", 
    "cities_visted": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 15},
]

def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["total_visits"] = visits
    new_country["cities_visited"] = cities
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)