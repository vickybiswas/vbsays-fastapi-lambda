from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def json_output():
  return {"output": "FastAPI is working"}

# End of File