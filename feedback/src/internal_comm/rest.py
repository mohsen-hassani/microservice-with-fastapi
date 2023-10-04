import requests
from .base import BaseInternalCommunication, InternalResponse, Statuses
from models.domains import UserID
from config import settings


class RestInternalCommunication(BaseInternalCommunication):
    def __init__(self):
        self.base_url = f"{settings.USER_SERVICE_BASE_URL}:{settings.USER_SERVICE_PORT}"

    def authenticate_user(self, user_token: str) -> UserID | None:
        endpoint = f"/internal/users/id"
        headers = {"Authorization": f"Bearer {user_token}"}
        response = self.send_request(endpoint, headers=headers)
        if response.status == Statuses.FAILED or response.status_code == 401:
            return None
        return response.body["id"]

    def send_request(
        self, endpoint: str, data: str = "", headers: dict = dict, method: str = "GET"
    ) -> InternalResponse:
        if endpoint.startswith("/"):
            endpoint = endpoint[1:]
        url = f"{self.base_url}/{endpoint}"
        requestor = getattr(requests, method.lower())
        try:
            response = requestor(url=url, data=data, headers=headers)
        except requests.RequestException as ex:
            return InternalResponse(status=Statuses.FAILED, exception=ex)
        try:
            response_body = response.json()
        except requests.exceptions.JSONDecodeError as ex:
            return InternalResponse(status=Statuses.FAILED, exception=ex)
        return InternalResponse(status_code=response.status_code, body=response_body, status=Statuses.OK)


