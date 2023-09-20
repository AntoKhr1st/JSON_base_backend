from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import uvicorn
from pysondb import db

app = FastAPI()

storage = db.getDb('/app/shared/documents.json')  # Инициализация базы данных pysondb


# Хранилище для JSON документов


@app.get("/documents/")
async def get_document(a_ids: list[int] = Query()):
    result = []
    for a_id in a_ids:
        document = storage.getByQuery({"article_id": a_id})
        if document:
            result.append(document)
    return result


# @app.post("/documents/")
# async def create_document(document):
#     storage.add(document)
#     return JSONResponse(content={"message": "Document created"})


if __name__ == "__main__":
    uvicorn.run("Fast_API:app", host="0.0.0.0", port=8000)
