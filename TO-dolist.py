#!/usr/bin/env python3

import json
from pathlib import Path

FILE = Path("todo.json")

def load_tasks():
    if FILE.exists():
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!\n")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["done"] else "Not Completed"
        print(f"{i}. [{status}] {task['title']}")
    print()

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print("Task added!")
    else:
        print("❗ Empty title not added.")

def mark_done(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to mark done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            save_tasks(tasks)
            print("Marked as done!")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def delete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Deleted: {removed['title']}")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def clear_tasks():
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == "y":
        save_tasks([])
        print("All tasks cleared!")

def main():
    tasks = load_tasks()

    while True:
        print("\nTO-DO MENU ")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Clear all tasks")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            tasks = load_tasks()
        elif choice == "3":
            mark_done(tasks)
            tasks = load_tasks()
        elif choice == "4":
            delete_task(tasks)
            tasks = load_tasks()
        elif choice == "5":
            clear_tasks()
            tasks = []
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("❗ Invalid choice, try again.")

if __name__ == "__main__":
    main()

