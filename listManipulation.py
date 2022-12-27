#1
students = ["Maria", "Nushi", "Mohammed", "Jose", "Yan"]

grades = [
    [9, 10, 8, 7, 10],
    [6, 7, 9, 10, 10],
    [10, 10, 9, 6, 8],
    [8, 8, 8, 9, 10],
    [10, 6, 5, 8, 10]
]
avg = []

for grade in grades:
    avg.append(sum(grade) / len(grade))

for i in range(len(students)):

    print("%-15s" % (students[i]), end='')

    for grade in grades[i]:
        print("%-5d " % (grade), end='')

    print("%-5.1f" % (avg[i]))

#2
nfl = {"Phoenix" "Atlanta", "Baltinore", "Buffalo", "Charlotte", "Chicago", "Cincinnati", "Cleveland", "Dallas",
"Denver", "Detroit", "Green Bay", "Houston", "Indianapolis", "Jacksonville", "Kansas City", "Las Vegas",
"Los Angeles", "Miami", "Minneapolis", "Boston", "New Orleans", "New York", "Philadelphia", "Pittsburgh",
"San Francisco", "Seattle", "Tampa Bay", "Nashville", "Tampa Bay", "Washington, D.C."}

mlb = {"Atlanta", "Miami", "New York", "Philadelphia", "Washington, D.C.", "Chicago", "Cincinnati", "Milwaukee",
"Pittsburgh", "St. Louis", "Phoenix", "Denver", "Los Angeles", "San Diego", "San Francisco", "Baltimore", "Boston",
"Tampa Bay", "Toronto", "Cleveland", "Detroit", "Kansas City", "Minneapolis", "Houston", "Oakland", "Seattle", "Dallas"}

common_city = nfl.intersection(mlb)

print('These cities have both an NFL & MLB team')
print(common_city)

#3
nfl = {"Phoenix" "Atlanta", "Baltinore", "Buffalo", "Charlotte", "Chicago", "Cincinnati", "Cleveland", "Dallas",
"Denver", "Detroit", "Green Bay", "Houston", "Indianapolis", "Jacksonville", "Kansas City", "Las Vegas",
"Los Angeles", "Miami", "Minneapolis", "Boston", "New Orleans", "New York", "Philadelphia", "Pittsburgh",
"San Francisco", "Seattle", "Tampa Bay", "Nashville", "Tampa Bay", "Washington, D.C."}


mlb = {"Atlanta", "Miami", "New York", "Philadelphia", "Washington, D.C.", "Chicago", "Cincinnati", "Milwaukee",
"Pittsburgh", "St. Louis", "Phoenix", "Denver", "Los Angeles", "San Diego", "San Francisco", "Baltimore", "Boston",
"Tampa Bay", "Toronto", "Cleveland", "Detroit", "Kansas City", "Minneapolis", "Houston", "Oakland", "Seattle", "Dallas"}


citiesNFL = nfl - nfl.intersection(mlb)

print('These cities have an NFL team but not and MLB team')
print(citiesNFL)


citiesMLB = mlb - nfl.intersection(mlb)

print('\nThese cities have an MLB team but not and NFL team')
print(citiesMLB)

#4
ivyMajors = {"Accounting": 325, "Entrepreneurship": 39, "Management": 400, "MIS": 290, "Supply Chain Management": 175}

for major, value in ivyMajors.items():
    print(major, ':', value)

#5
top10 = {"@BarackObama": 133.4, "@elonmusk": 114.6, "@justinbieber": 113.8, "@katyperry": 108.9, "@rihanna": 107, "@Cristiano": 104.5, "@taylorswift13": 91.5, "@ladygaga": 84.9, "@narendramodi": 84.1, "@TheEllenShow": 77.2}

print(top10)

top10["@BarackObama"] = 134.3
del top10["@elonmusk"]
top10["@KimKardashian"] = 73.9



print(top10)
