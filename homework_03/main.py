from fastapi import FastAPI

app = FastAPI()

@app.get("/ping/", status_code=200, response_model=dict)
def ping():
    return {"message": "pong"}