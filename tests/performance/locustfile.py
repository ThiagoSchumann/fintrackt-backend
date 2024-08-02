# tests/performance/locustfile.py

from locust import HttpUser, TaskSet, task, between

class AccountTasks(TaskSet):
    @task
    def create_account(self):
        self.client.post("/accounts", json={"name": "Performance Test Account"})

    @task
    def get_account(self):
        self.client.get("/accounts/1")

    @task
    def update_account(self):
        self.client.put("/accounts/1", json={"name": "Updated Performance Test Account"})

    @task
    def delete_account(self):
        self.client.delete("/accounts/1")

class WebsiteUser(HttpUser):
    tasks = [AccountTasks]
    wait_time = between(1, 5)
    host = "http://localhost:5000"  # Adicione a URL base do seu host aqui
