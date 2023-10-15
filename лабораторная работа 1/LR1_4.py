users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
poseheniya = {"Общее количество" : 0,
              "Уникальные посещения" : 0}
poseheniya["Общее количество"] = len(users)
poseheniya["Уникальные посещения"] = len(set(users))
print(poseheniya)
