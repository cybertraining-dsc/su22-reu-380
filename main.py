from fastapi import FastAPI
app = FastAPI()
#
# @app.get("/")
# async def root():
#     return {"processor": "5950X"}


# @app.get("/temperature")
# async def temperature():
#     return {"temperature": 0}

@app.get("/temperature/{temp_id}")
async def temperature(temp_id: int):
    return {"temperature": temp_id}

# from fastapi import FastAPI
# my_awesome_app = FastAPI()
#
# @my_awesome_app.get("/")
# async def root():
#     return {"beige": "5950X"}



