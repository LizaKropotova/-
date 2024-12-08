# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):

    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))
    common_participants = sorted(participants1.intersection(participants2))
    return common_participants
group1 = "Иванов,Петров,Сидоров"
group2 = "Петров,Сидоров,Смирнов"
common = find_common_participants(group1, group2)
print(common)