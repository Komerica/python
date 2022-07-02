travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above
print(travel_log[0]['cities'][0])  # 👉 Paris
# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country_visited, times_visited, cities_visited):
    new_dictionary = {}
    new_dictionary["country"] = country_visited
    new_dictionary["visits"] = times_visited
    new_dictionary["cities"] = cities_visited
    travel_log.append(new_dictionary)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
