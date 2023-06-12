
# main.py
import uvicorn
from fastapi import FastAPI
from collections.crud import get_collection, post_collection
from collections.schema import CollectionSchema
from collections.collection import Collection

app = FastAPI()

@app.get("/collection/")
def get_collection():
    return get_collection()

@app.post("/collection/")
def post_collection(collection: CollectionSchema):
    return post_collection(collection)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)