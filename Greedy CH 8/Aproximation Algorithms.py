# O(N**2)=(N*N)
states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])
stations = {}
stations["kOne"] = set(["id","nv","ut"])
stations["kTwo"] = set(["wa","id","mt"])
stations["kThree"] = set(["or","nv","ca"])
stations["kFour"] = set(["nv","ut"])
stations["kFive"] = set(["ca","az"])

final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states # & intersection
        print(covered)
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
print("\nThe final stations is " , final_stations)