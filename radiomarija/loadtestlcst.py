from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "radiomaria.nordweb1.in.rs"
    wait_time = between(1, 3)

@task
def index(self):
    self.client.get("/")