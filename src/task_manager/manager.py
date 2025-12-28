class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = {"id": self.next_id, "description": description, "done": False}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def delete_task(self, task_id):
        task_to_remove = None
        for task in self.tasks:
            if task["id"] == task_id:
                task_to_remove = task
                break
        if task_to_remove:
            self.tasks.remove(task_to_remove)
            return True
        return False

    def mark_done(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                return True
        return False

    def list_tasks(self):
        return self.tasks.copy()
