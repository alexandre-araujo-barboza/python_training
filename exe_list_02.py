# Exercício - Lista de tarefas com desfazer e refazer

import json, os

tasks = []
tasks_to_redo = []
filename = 'tasks.json'

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
  show(tasks)

def redo(tasks, tasks_to_redo):
  print()
  if not tasks_to_redo:
    print('No tasks to redo!')
    return
  task = tasks_to_redo.pop()
  print(f'{task=} added to the task list.')
  tasks.append(task)
  print()
  show(tasks)

def add(tasks, task):
  print()
  task = task.strip()
  if not task:
    print('You have not entered a task!')
    return
  print(f'{task=} added to the task list.')
  tasks.append(task)
  print()
  show(tasks)

def load(tasks,path):
  data = []
  try:
    with open(path, 'r', encoding='utf8') as file:
      data = json.load(file)
      for value in data:
        tasks.append(value)
      print()
      print("file was loaded.")
  except FileNotFoundError:
    print()
    print('File not found!')
  except json.decoder.JSONDecodeError:
    print()
    print('File was corrupted!')

def save(tasks, path):
  data = tasks
  with open(path, 'w', encoding = 'utf8') as file:
    data = json.dump(tasks, file, indent=2, ensure_ascii=False)
  tasks = data
  print()
  print("file was saved.")

def destroy(tasks):
  tasks.clear()
  print()
  print("tasks is empty.")
  
def clear():
  os.system('cls')

def quit():
  print("Bye!")
  print()  
  os.system(exit())

while True:
  print('Commands: show, undo, redo, load, save, destroy, clear and quit')
  task = input('Enter a task or command: ')
  commands= {
    'show' : lambda: show(tasks),
    'undo' : lambda: undo(tasks, tasks_to_redo),
    'redo' : lambda: redo(tasks, tasks_to_redo),
    'add'  : lambda: add(tasks, task),
    'load' : lambda: load(tasks,filename),
    'save' : lambda: save(tasks, filename),
    'destroy' : lambda : destroy(tasks),
    'clear': lambda: clear(),
    'quit' : lambda: quit(),

  }
  
  command = commands.get(task) if commands.get(task) is not None else \
  commands['add']
  command()

  