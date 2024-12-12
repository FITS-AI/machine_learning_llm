from app.inference import get_prediction
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hi Fitizen. Welcome to FITS! Your personal food advisor"}

# Request model
class PromptRequest(BaseModel):
    prompt: str

@app.post("/prompt")
def generate_response(request: PromptRequest):
    try:
        response = get_prediction(request.prompt)
        return {"success": True, "data": response}
    except Exception as e:
        return {"success": False, "error": str(e)}
