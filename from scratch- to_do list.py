#day 2, today we will build the to-do list app from scratch. We will be using Python

print("Welcome to the To-Do List App!\n")
print("i will boost you todays journy with a little help, so you can create your own to-do list app from scratch.\n")


todo_list = []
done_list = []

num_of_tasks = int(input("how many task you have for today?: "))

for i in range (num_of_tasks):
    task=input(f"enter the task: {i+1} ")
    todo_list.append(task)

while len(todo_list)>0:
    print("your pending tasks are: ")

    for index, task in enumerate(todo_list):
        print(index,"-->",task)

    done=int(input("enter the index of the task you have completed: "))

    finished= todo_list.pop(done)
    done_list.append(finished)

    print(f"Great! You completed: {finished}")

if len(todo_list) == 0:
    print("\n🎉 All tasks completed for today!")
    print("You did amazing today. Small progress is still progress.")
    print("Rest well and come back stronger tomorrow ❤️")

'''This project shows the use of list, for loop, while loop and if else statements in python
we can understand how while loop is working until the condition is true "while len(todo_list)>0"
we have also used f string to print the completed task and the pending tasks for the day
and we have used enumerate to get the index of the task in the list and print it along with the task name'''

