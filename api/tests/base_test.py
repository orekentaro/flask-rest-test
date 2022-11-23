class BaseTest:
    def login(self, client):
        with client:
            client.post(
                "/auth/", data={"email": "test@test.test", "password": "password123"}
            )
