from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def json_output():
  return {"output": "FastAPI is working"}

@app.get("/route")
async def route():
    return {"output": "Another FastAPI route"}

# End of File