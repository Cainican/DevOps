# Using json to save to_do_list
import os
import json
from datetime import datetime

# Main program loop
def main():
  tasks = []
  # Make it a loop, until we press exit
  while True:
    print('============== To-Do-List ==============\n'
    '1. Add task\n'
    '2. Add task with priority and timestamp\n'
    '3. Edit task\n'
    '4. Show tasks\n'
    '5. Mark task/s as Done\n'
    '6. Delete task/s\n'
    '7. Save/load/delete task using JSON\n'
    '8. Exit\n')

    choice = input('Enter your choice: ').strip()

    # Add task
    if choice == '1':
      try:
        n_tasks = int(input('How many task/s do you want to add: '))
        for i in range(n_tasks):
          task = input('Enter the task: ')
          priority = input('Enter priority (High/Medium/Low or leave blank): ').capitalize()
          task_data = {'task': task, 'Done': False}
          if priority:
            task_data['Priority'] = priority
            task_data['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          tasks.append(task_data)
          print('Task added')
      except ValueError:
        print('Invalid number. Please enter a valid integer')

    # Add task with priority and timestamp
    elif choice == '2':
      try:
        task = input('Enter the task: ')
        priority = input('Enter priority (High/Medium/Low): ').capitalize()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tasks.append({
          'task': task,
          'Done': False,
          'Priority': priority,
          'Timestamp': timestamp
        })
        print('Task with priority and timestamp added')
      except Exception as e:
        print(f'Error adding task: {e}')

    # Edit task
    elif choice == '3':
      if not tasks:
        print('No tasks to edit')
        continue
      try:
        task_index = int(input('Enter the task number to edit: ')) - 1
        if 0 <= task_index < len(tasks):
          new_task = input('Enter the new task description: ')
          new_priority = input('Enter new priority (High/Medium/Low or leave blank): ').capitalize()
          update_time = input('Update timestamp to now? (y/n): ').strip().lower()
          tasks[task_index]['task'] = new_task
          if new_priority:
            tasks[task_index]['Priority'] = new_priority
          if update_time == 'y':
            tasks[task_index]['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          print('Task updated')
        else:
          print('Invalid task number')
      except ValueError:
        print('Invalid input. Please enter a number')

    # Show tasks
    elif choice == '4':
      if tasks:
        print('Tasks:')
        for index, task in enumerate(tasks):
          status = 'Done' if task['Done'] else 'Not Done'
          priority = task.get('Priority', 'N/A')
          timestamp = task.get('Timestamp', 'N/A')
          print(f'{index + 1}. {task["task"]} - {status} | Priority: {priority} | Added: {timestamp}\n')
      else:
        print('No tasks to show')

    # Mark task/s as done
    elif choice == '5':
      try:
        task_index = int(input('Enter the task number you want as done: ')) - 1
        if 0 <= task_index < len(tasks):
          tasks[task_index]['Done'] = True
          print('Task marked as Done')
        else:
          print('Invalid task number')
      except ValueError:
        print('Invalid input. Please enter a number')

    # Delete task
    elif choice == '6':
      if not tasks:
        print('No tasks to delete')
        continue
      print('\nTasks:')
      for index, task in enumerate(tasks):
        status = 'Done' if task['Done'] else 'Not Done'
        print(f'{index + 1}. {task["task"]} - {status}')
      n_delete = input('Enter the task/s you want to delete (comma-separated): ')
      try:
        indices = [int(i.strip()) - 1 for i in n_delete.split(',')]
        indices = sorted(set(indices), reverse=True)
        for i in indices:
          if 0 <= i < len(tasks):
            task_name = tasks[i]['task']
            confirm = input(f'Are you sure you want to delete "{task_name}"? (y/n): ').strip().lower()
            if confirm == 'y':
              deleted = tasks.pop(i)
              print(f'Task: "{deleted["task"]}" deleted')
            else:
              print(f'Task "{task_name}" not deleted')
          else:
            print(f'Task number {i + 1} is out of range')
      except ValueError:
        print('Invalid input. Please enter numbers separated by commas')

    # Save/load/delete task using json
    elif choice == '7':
      print('\n1. Save tasks to JSON\n'
      '2. Load tasks from JSON\n'
      '3. Delete a saved JSON file\n')
      sub_choice = input('Enter your choice (1, 2 or 3): ').strip()
      # Save task/s
      if sub_choice == '1':
        filename = input('Enter filename to save (e.g., tasks.json): ').strip()
        try:
          with open(filename, 'w') as f:
            json.dump(tasks, f, indent=2)
          print(f'Tasks saved to {filename}')
        except Exception as e:
          print(f'Error saving tasks: {e}')

      # Load task/s
      elif sub_choice == '2':
        filename = input('Enter filename to load (e.g., tasks.json): ').strip()
        try:
          with open(filename, 'r') as f:
            tasks = json.load(f)
          print(f'Tasks loaded from {filename}')
        except FileNotFoundError:
          print(f'File not found. Please check the filename')
        except json.JSONDecodeError:
          print(f'File is not a valid json')
        except Exception as e:
          print(f'Error loading tasks: {e}')

      # Delete saved file
      elif sub_choice == '3':
        filename = input('Enter filename to delete (e.g., tasks.json): ').strip()
        if os.path.exists(filename):
          confirm = input(f'Are you sure you want to delete "{filename}"? (y/n): ').strip()
          if confirm == 'y':
            try:
              os.remove(filename)
              print(f'File "{filename}" deleted successfully\n')
            except Exception as e:
              print(f'Error deleting file {e}\n')
          else:
            print('File not deleted\n')
        else:
          print('File does not exist\n')
      else:
        print('Invalid choice. Please enter 1, 2 or 3\n')

    # Exit the To-Do-List
    elif choice == '8':
      confirm_exit = input('Do you want to save your task/s before exiting? (y/n): ').strip().lower()
      if confirm_exit == 'y':
        filename = input('Enter filename to save (e.g., tasks.json): ').strip()
        try:
          with open(filename, 'w') as f:
            json.dump(tasks, f, indent=2)
          print(f'Task/s saved to {filename}')
        except Exception as e:
          print(f'Error saving task/s: {e}')
      print('Exiting the To-Do-List')
      break

if __name__ == '__main__':
  main()