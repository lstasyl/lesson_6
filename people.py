people = [{"name": "John", "age": 15}, 
          {"name": "Jacson", "age": 28},
          {"name": "Emily", "age": 42},
          {"name": "Brandon", "age": 19},
          {"name": "Olivia", "age": 35},
          {"name": "Ethan", "age": 50},
          {"name": "Sophia", "age": 23},
          {"name": "Caleb", "age": 39},
          {"name": "Ava", "age": 31},
          {"name": "Mason", "age": 56},
          {"name": "Grace", "age": 26},
          {"name": "Jack", "age": 45},
          ]

#young_person
person = min(people, key=lambda x: x["age"])
young_person = [person["name"]]
print(young_person)

#long_name
long_name = None
max_length = 0


for name in people:
    for key, value in name.items():
        if isinstance(value, str):
            words = value.split()
            for word in words:
                if len(word) > max_length:
                    long_name = word
                    max_length = len(word)

long_name_list = [long_name]

print(long_name_list)
print("Length:", max_length)

#

all_age = [entry["age"] for entry in people]
sum_age = sum(all_age) / len(all_age)

print(int(sum_age))


