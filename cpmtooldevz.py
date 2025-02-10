import requests

__ENDPOINT_URL__ = "https://testers.squareweb.app/api"

class CPMTooldevz:
    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key

    def login(self, email, password) -> int:
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/account_login", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")

    def register(self, email, password) -> int:
        payload = {"account_email": email, "account_password": password}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/account_register", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("error")

    def delete(self):
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        requests.post(f"{__ENDPOINT_URL__}/account_delete", params=params, data=payload)

    def get_player_data(self) -> any:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/get_data", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded

    def set_player_rank(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/set_rank", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_money(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/set_money", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_coins(self, amount) -> bool:
        payload = {"account_auth": self.auth_token, "amount": amount}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/set_coins", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def get_player_car(self, car_id) -> any:
        payload = {"account_auth": self.auth_token, "car_id": car_id}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/get_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded

    def hack_car_speed(self, car_id) -> bool:
        payload = {"account_auth": self.auth_token, "car_id": car_id}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/hack_car_speed", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def car_set_steering_angle(self, car_id, angle) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "car_id": car_id,
            "steering_angle": angle
        }
        params = {"key": self.access_key}
        
        response = requests.post(f"{__ENDPOINT_URL__}/car_set_steering_angle", params=params, data=payload)

        try:
            response_decoded = response.json()
            return response_decoded.get("ok", False)
        except requests.exceptions.JSONDecodeError:
            return False
        except requests.exceptions.RequestException:
            return False

    def unlock_all_cars(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_all_cars", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_wheels(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_wheels", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_smoke(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_smoke", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_paid_cars(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_paid_cars", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_houses(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_houses", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_equipments_male(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_equipments_male", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_equipments_female(self) -> bool:
        payload = {"account_auth": self.auth_token}
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_equipments_female", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def account_clone(self, account_email, account_password) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "account_email": account_email,
            "account_password": account_password
        }
        params = {"key": self.access_key}
        response = requests.post(f"{__ENDPOINT_URL__}/clone", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
