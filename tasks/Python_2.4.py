"""
2.4.1 Create good script to create new list, which only contains users from Poland. Try to do it
      with List Comprehension.
      users = [{"name": "Kamil", "country":"Poland", {"name":"John", "country": "USA"}, {"name":
      "Yeti"}]

2.4.2 Display sum of first ten elements starting from element 5:
      numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123]

2.4.3 Fill list with powers of 2, n [1..20]
"""

# 2.4.1
users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}]
users_from_poland = [user for user in users if 'country' in user.keys() and user['country'] == 'Poland']

# 2.4.2
numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]
sum_of_numbers = sum(numbers[numbers.index(5):11])

# 2.4.3
numbers_powers_2 = [number ** 2 for number in range(1, 21)]

if __name__ == "__main__":
    print(users_from_poland)
    print(sum_of_numbers)
    print(numbers_powers_2)

