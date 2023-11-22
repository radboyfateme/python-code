from collections import Counter


student_list1 = [
    {"Name": "Ali Rezaee", "Age": 25}, {"Name": "Reza Ahmadi", "Age": 28},
    {"Name": "Sara Akbari", "Age": 25}, {"Name": "Bahar Najafi", "Age": 23},
    {"Name": "Iman Mohamadi", "Age": 25}, {"Name": "Sima Shaker", "Age": 25},
    {"Name": "Negin Ghazi", "Age": 29}, {"Name": "Maryam Yaghoubi", "Age": 25},
    {"Name": "Mitra Sharif", "Age": 23}, {"Name": "Ahmad Moradi", "Age": 25}
]

student_list2 = [
    {"Name": "Amir Radi", "Age": 23}, {"Name": "Reza Ardakani", "Age": 23},
    {"Name": "Sima Sadr", "Age": 26}, {"Name": "Bahman Najafi", "Age": 30},
    {"Name": "Mina Mohamadi", "Age": 23}, {"Name": "Mitra Moradi", "Age": 23},
    {"Name": "Narges Arab", "Age": 30}, {"Name": "Ali Eshtiyaghi", "Age": 32}
]

def most_common_age(student_list):
    age_counter = Counter(student['Age'] for student in student_list)
    return age_counter.most_common(1)[0]


most_common_age_group1 = most_common_age(student_list1)
most_common_age_group2 = most_common_age(student_list2)

print("Output")
print("------------------")
print(f"Group1: {most_common_age_group1}")
print(f"Group2: {most_common_age_group2}")

