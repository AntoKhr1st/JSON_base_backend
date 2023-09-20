from typing import List
from pydantic import BaseModel


class Location(BaseModel):
    lat: float
    lon: float


class Article(BaseModel):
    article_id: int
    text: str
    title: str
    date: str
    lang: str
    locations: List[Location]
    semantic_vector: List[float]
    keywords: List[str]
    entities: List[str]
    themes: List[str]
    class_: List[str] = []

# {
# 	"article_id": 12343454462,
# 	"text": "Текст публикации...",
#     "title": "Заголовок публикации",
#     "date": "2022-03-25 12:14:00",
#     "lang": "ru",
#     "locations": [
#     	{
#             "lat": 41.12,
# 			"lon": -71.34
#         },
#         {
#             "lat": 47.16,
# 			"lon": -72.82
#         }
#     ],
#     "semantic_vector": [0.1, 0.03, 0.20 .... n], # вектор 512 значений
#     "keywords": ['keyword1', 'keyword2', 'keyword3', .... 'keywordn'],
#     "entities": ['entity1_loc', 'entity2_per', 'entity_part1 entity_part2_work_of_art'],
#     "themes": ["7585dfb5-cd1c-4f55-8775-6a2c48afc371", "7f2bfdd8-efbc-454d-ad62-c6d9351e7b77", ... n],
#     "class": ["7585dfb5-cd1c-4f55-8775-6a2c48afc371", "7f2bfdd8-efbc-454d-ad62-c6d9351e7b77", ... n]
# }
