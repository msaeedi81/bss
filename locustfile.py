from locust import HttpUser, between, task
import random


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        username = random.choice(['user1', 'user2', 'user3'])
        password = 'password123'

        response = self.client.post("/auth/token/", json={"username": username, "password": password})

        if response.status_code == 200:
            self.token = response.json()["access"]
            print(f"Authenticated user: {username}")
        else:
            print(
                f"Failed to authenticate user: {username}. Status code: {response.status_code}, Response: {response.text}")

    @task
    def score_content(self):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        content_list_response = self.client.get("/score/content/list/", headers=headers)
        print(content_list_response.json())

        if content_list_response.status_code == 200:
            content_list = content_list_response.json()

            if content_list:
                content = random.choice(content_list)
                content_id = content['id']

                payload = {
                    "content_id": content_id,
                    "score": random.randint(1, 5),
                }

                score_response = self.client.post("/score/content/score/", headers=headers, json=payload)

                if score_response.status_code == 200:
                    print(f"Successfully scored content with ID {content_id}")
                else:
                    print(
                        f"Failed to score content. Status: {score_response.status_code}, Response: {score_response.text}")
            else:
                print("No content available to score.")
        else:
            print(
                f"Failed to fetch content list. Status: {content_list_response.status_code}, Response: {content_list_response.text}")
