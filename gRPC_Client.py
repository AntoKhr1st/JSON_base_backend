import grpc


# Import the generated classes
import gen.storage_pb2
import gen.storage_pb2_grpc


def upload_documets(documents):
    # Initialize a channel
    channel = grpc.insecure_channel('localhost:50051')

    # Create a stub (client)
    stub = gen.storage_pb2_grpc.DocumentServiceStub(channel)
    response = None

    for doc in documents:
        locations = [
            gen.storage_pb2.Location(lat=location["lat"], lon=location["lon"])
            for location in doc["locations"]
        ]

        doc_unit = gen.storage_pb2.Document(
            article_id=doc["article_id"],
            text=doc["text"],
            title=doc["title"],
            date=doc["date"],
            lang=doc["lang"],
            locations=locations,
            semantic_vector=doc["semantic_vector"],
            keywords=doc["keywords"],
            entities=doc["entities"],
            themes=doc["themes"],
            class_=doc["class_"]
        )

        request = gen.storage_pb2.InsertRequest(documents=[doc_unit])

        # Make a request
        response = stub.SaveDocuments(request)

    return response




