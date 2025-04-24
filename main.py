from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/count")
def count(request: Request):
    data = request.json()
    print(data)
    return {"message": "Hello World2"}
