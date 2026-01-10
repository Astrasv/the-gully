import uuid

from pydantic import BaseModel


class ChatBase(BaseModel):
    user_message: str


class ChatCreate(ChatBase):
    pass


class Chat(ChatBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    agent_response: str

    class Config:
        orm_mode = True
