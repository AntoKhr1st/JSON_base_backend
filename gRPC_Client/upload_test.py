from gRPC_Client import upload_documets

data_test = [
    {
        "article_id": 1010,
        "text": "Sample text",
        "title": "Sample title",
        "date": "1970-02-03T20:14:05.255549665Z",
        "lang": "en",
        "locations": [
            {
                "lat": 1.0,
                "lon": 1.0
            },
            {
                "lat": 2.0,
                "lon": 2.0
            },
            {
                "lat": 3.0,
                "lon": 3.0
            },
            {
                "lat": 4.0,
                "lon": 4.0
            },
            {
                "lat": 4.0,
                "lon": 4.0
            }
        ],
        "semantic_vector": [0.1, 0.2],
        "keywords": ["sample", "test"],
        "entities": ["entity1", "entity2"],
        "themes": ["theme1", "theme2"],
        "class_": ["class1", "class2"]
    },
    {
        "article_id": -1010,
        "text": "Sample text",
        "title": "Sample title",
        "date": "1970-02-03T20:14:05.255549665Z",
        "lang": "en",
        "locations": [
            {
                "lat": 1.0,
                "lon": 1.0
            },
            {
                "lat": 2.0,
                "lon": 2.0
            },
            {
                "lat": 3.0,
                "lon": 3.0
            },
            {
                "lat": 4.0,
                "lon": 4.0
            },
            {
                "lat": 4.0,
                "lon": 4.0
            }
        ],
        "semantic_vector": [0.1, 0.2],
        "keywords": ["sample", "test"],
        "entities": ["entity1", "entity2"],
        "themes": ["theme1", "theme2"],
        "class_": ["class1", "class2"]
    }
]

test = upload_documets(data_test)
if test.success:
    print(f"Insertion successful: {test.message}")
else:
    print(f"Insertion failed: {test.message}")
