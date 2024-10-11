from fastapi import FastAPI
from pydantic import BaseModel
from llm import get_llm
from prompt import get_chat_prompt_template
from chain import create_chain
import uvicorn

app = FastAPI()


llm = get_llm()
prompt = get_chat_prompt_template()
chain = create_chain(llm, prompt)

class ChatRequest(BaseModel):
    content: str


@app.post("/chat")
async def chat(request: ChatRequest):
    response = ""
    async for res in chain.astream({"content": request.content}):
        response += res
    return {"response": response}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
