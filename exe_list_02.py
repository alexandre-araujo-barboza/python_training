def show(tasks):
  print()
  if not tasks:
    print('no tasks to show!')
    return

  print('Tasks:')
  for task in tasks:
    print(f'\t{task}')
  print()

def undo(tasks, tasks_to_redo):
  print()
  if not tasks:
    print('No tasks to undo!')
    return

  task = tasks.pop()
  print(f'{task=} removed from the task list.')
  tasks_to_redo.append(task)
  print()

def redo(tasks, tasks_to_redo):
  print()
  if not tasks_to_redo:
    print('No tasks to redo!')
    return

  task = tasks_to_redo.pop()
  print(f'{task=} added to the task list.')
  tasks.append(task)
  print()

def add(tasks, task):
  print()
  task = task.strip()
  if not task:
    print('You have not entered a task!')
    return
  print(f'{task=} added to the task list.')
  tasks.append(task)
  print()

tasks = []
tasks_to_redo = []

while True:
  print('Commands: show, undo, redo and quit')
  task = input('Enter a task or command: ')
  if task == 'undo':
    undo(tasks, tasks_to_redo)
  elif task == 'redo':
    redo(tasks, tasks_to_redo)
  elif task == 'quit':
    break
  else:
    add(tasks, task)
 
  show(tasks)

print("Bye!")  
  