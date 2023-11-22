from itertools import chain, islice, combinations


expert_list1 = [("Ali","Ahmadi","M",35), ("Sima","Sadri","C",39), 
                ("Ahmad","Moradi","M",30), ("Fatemeh","Majd","C",29), ("Sara","Biglar","IE",27), 
                ("Reza","Rahnama","EE",45)]
expert_list2 = [("Mina","Gohari","EE",40), ("Iman","Shams","M",26), 
                ("Farzad","Yeganeh","M",41), ("Ali","Imani","C",33), ("Aref","Alameh","M",32), 
                ("Narges","Sohrabi","C",35)]


combined_experts = sorted(chain(expert_list1, expert_list2), key=lambda x: x[2])

print("Sorted Combined Expert List:")
for expert in combined_experts:
    print(expert)

math_experts = [expert for expert in combined_experts if expert[2] == "M"]
math_groups = list(islice(combinations(math_experts, 3), len(math_experts) // 3))


print("\nMath Expert Groups:")
for group in math_groups:
    print(group)

