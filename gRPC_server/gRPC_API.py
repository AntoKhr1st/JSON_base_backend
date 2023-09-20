from concurrent import futures
import grpc
import gen.storage_pb2
import gen.storage_pb2_grpc
from pysondb import db


class DocumentService(gen.storage_pb2_grpc.DocumentServiceServicer):
    def __init__(self):
        self.storage = db.getDb('/app/shared/documents.json')
        print('bd up')

    def SaveDocuments(self, request, context):
        for document in request.documents:
            article = {
                'article_id': document.article_id,
                'text': document.text,
                'title': document.title,
                'date': document.date,
                'lang': document.lang,
                'locations': [{
                    'lat': location.lat,
                    'lon': location.lon
                } for location in document.locations],
                'semantic_vector': list(document.semantic_vector),
                'keywords': list(document.keywords),
                'entities': list(document.entities),
                'themes': list(document.themes),
                'class_': list(document.class_)
            }
            self.storage.add(article)
        return gen.storage_pb2.InsertResponse(success=True, message="Documents saved successfully")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gen.storage_pb2_grpc.add_DocumentServiceServicer_to_server(DocumentService(), server)
    # Измените адрес и порт прослушивания на локальный хост и порт, на котором работает Nginx
    # server.add_secure_port("[::]:50051", grpc.ssl_server_credentials())  # Используем безопасное соединение
    server.add_insecure_port("[::]:50051")
    server.start()
    print('server up')
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
