from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/authorization/sign_up")
async def signup_page():
    return


@app.post("/authorization/signup")
async def signup_page():
    return


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main_server:app", host="127.0.0.1", port=8000, reload=True)
