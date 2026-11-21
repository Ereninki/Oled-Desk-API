import uvicorn
from fastapi import HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=["*"]
)

@app.get("/")
async def health():
    return {"health": "OK"}

if __name__ == "__main__":
    uvicorn.run(app)