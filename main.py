from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://yandex.ru"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    
    allow_credentials=True,     
    allow_methods=["*"],     
    allow_headers=["*"],       
)

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "Timeweb Cloud + FastAPI = ❤️"
