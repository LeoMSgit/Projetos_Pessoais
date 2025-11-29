from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv


load_dotenv()


from agent import ChatAgent


app = FastAPI()


class ChatRequest(BaseModel):
message: str


class ChatResponse(BaseModel):
response: str


# instancia o agente uma vez ao iniciar o servidor
agent = ChatAgent()


@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest):
try:
resp = agent.handle_message(payload.message)
return ChatResponse(response=resp)
except Exception as e:
raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
import uvicorn
uvicorn.run("main:app", host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", 8000)), reload=True)
