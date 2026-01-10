import uuid
from typing import Any

from fastapi import APIRouter, HTTPException

from app import crud
from app.api import deps
from app.schemas.chat import Chat, ChatCreate

router = APIRouter()


@router.post("/", response_model=Chat)
def create_chat(
    *,
    session: deps.SessionDep,
    chat_in: ChatCreate,
    current_user: deps.CurrentUser,
) -> Any:
    """
    Create new chat.
    """
    chat = crud.create_chat(
        session=session, chat_in=chat_in, user_id=current_user.id
    )
    return chat


@router.get("/", response_model=list[Chat])
def read_chats(
    *,
    session: deps.SessionDep,
    current_user: deps.CurrentUser,
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve chats.
    """
    chats = crud.get_chats_by_user(
        session=session, user_id=current_user.id, skip=skip, limit=limit
    )
    return chats


@router.delete("/{chat_id}", response_model=Chat)
def delete_chat(
    *,
    session: deps.SessionDep,
    current_user: deps.CurrentUser,
    chat_id: uuid.UUID,
) -> Any:
    """
    Delete a chat.
    """
    chat = crud.get_chat_by_id_and_user_id(
        session=session, chat_id=chat_id, user_id=current_user.id
    )
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    crud.delete_chat(session=session, chat=chat)
    return chat
