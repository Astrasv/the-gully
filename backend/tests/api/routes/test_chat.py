
from fastapi.testclient import TestClient

from app.core.config import settings


def test_create_chat(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.post(
        f"{settings.API_V1_STR}/chat/",
        headers=superuser_token_headers,
        json={"user_message": "Hello"},
    )
    assert response.status_code == 200
    content = response.json()
    assert content["user_message"] == "Hello"
    assert "agent_response" in content
    assert "id" in content
    assert "owner_id" in content


def test_read_chats(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/chat/", headers=superuser_token_headers
    )
    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)
    if content:
        assert "user_message" in content[0]
        assert "agent_response" in content[0]
        assert "id" in content[0]
        assert "owner_id" in content[0]


def test_delete_chat(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    # Create a chat to delete
    response = client.post(
        f"{settings.API_V1_STR}/chat/",
        headers=superuser_token_headers,
        json={"user_message": "Delete me"},
    )
    assert response.status_code == 200
    chat_to_delete = response.json()
    chat_id = chat_to_delete["id"]

    # Delete the chat
    response = client.delete(
        f"{settings.API_V1_STR}/chat/{chat_id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    deleted_chat = response.json()
    assert deleted_chat["id"] == chat_id
    assert deleted_chat["user_message"] == "Delete me"

    # Verify the chat is deleted
    response = client.get(
        f"{settings.API_V1_STR}/chat/", headers=superuser_token_headers
    )
    assert response.status_code == 200
    content = response.json()
    assert chat_id not in [c["id"] for c in content]


def test_delete_other_users_chat(
    client: TestClient,
    superuser_token_headers: dict[str, str],
    normal_user_token_headers: dict[str, str],
) -> None:
    # Create a chat with superuser
    response = client.post(
        f"{settings.API_V1_STR}/chat/",
        headers=superuser_token_headers,
        json={"user_message": "Superuser chat"},
    )
    assert response.status_code == 200
    chat_to_delete = response.json()
    chat_id = chat_to_delete["id"]

    # Try to delete with normal user
    response = client.delete(
        f"{settings.API_V1_STR}/chat/{chat_id}",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 404
