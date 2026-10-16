total_chores = 4
original_count = total_chores
print(f"you have {original_count } chores to finish today!")
comepleted_count= 0
chore_num = 1
while chore_num <= total_chores:

    if chore_num  == 1: next_chore ="make ur bed"
    elif chore_num == 2:next_chore = "feed the pet"
    elif chore_num == 3:next_chore = "take out trash"
    else: next_chore = "wash the dishes"

answer = input(f"have u finished :(next_chore)? (yes/no)")
if answer =="yes":
    comepleted_count += 1
    chore_num += 1
    print("great job chore completed")
else:
    print("okey,finish it and check again")

print("chores remaining:",total_chores - comepleted_count)
print()

print("---All chores completed---")
print("great work finishing your entire checklist today")

print("now lets safely peek at an infinite loop...")
test_value = 0
safety_counter = 0
while test_value <=0:
    print("this condition never changes,so  this world run forever!")
    safety_counter +=1
    if safety_counter == 3:
        print("stopping here on purpose - a real infinite loop never stops on its own")
        break

print(" chores completed good",original_count,comepleted_count,total_chores - comepleted_count)


    
