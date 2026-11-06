from fastapi import FastAPI

app = FastAPI(title="Tutor Platform API")

@app.get("/")
async def health_check():
    return {
        "status": "ok",
        "message": "Платформа для репетиторов и учеников запущена"
    }
