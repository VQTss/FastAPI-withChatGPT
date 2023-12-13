from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from loguru import logger
from utils import query_agent, create_agent

app = FastAPI()
security = HTTPBasic()

agent = create_agent("data/products.csv")

@app.post("/chat")
async def chat(
    text: str
):
    logger.info(f"User: {text}")
    response = query_agent(agent, text)
    return {"response": response}

# Please read more about this here
# https://fastapi.tiangolo.com/advanced/security/http-basic-auth/
@app.post("/chat-auth")
async def chat(
    text: str,
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    if credentials.username != "thaivq" or credentials.password != "thai":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    logger.info(f"User: {text}")
    response = query_agent(agent, text)
    return {"response": response}
