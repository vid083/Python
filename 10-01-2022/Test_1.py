
travel = {
          "country" : "ïndia",
          "cities_visited" : ["hyd", "chennai", "banglore"],
          "total_visits" : 15
        }
# a=travel.values()
# print(a)

for key,values in travel.items():
    # value = travel[key]
    print(key,values)
    # print(travel[key])

travel["capital"] = "Delhi"
print(travel)

travel["total_visits"] = 18
print(travel)
