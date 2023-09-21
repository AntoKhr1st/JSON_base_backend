from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Location(_message.Message):
    __slots__ = ["lat", "lon"]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    lat: float
    lon: float
    def __init__(self, lat: _Optional[float] = ..., lon: _Optional[float] = ...) -> None: ...

class Document(_message.Message):
    __slots__ = ["article_id", "text", "title", "date", "lang", "locations", "semantic_vector", "keywords", "entities", "themes", "class_"]
    ARTICLE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_VECTOR_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    THEMES_FIELD_NUMBER: _ClassVar[int]
    CLASS__FIELD_NUMBER: _ClassVar[int]
    article_id: int
    text: str
    title: str
    date: str
    lang: str
    locations: _containers.RepeatedCompositeFieldContainer[Location]
    semantic_vector: _containers.RepeatedScalarFieldContainer[float]
    keywords: _containers.RepeatedScalarFieldContainer[str]
    entities: _containers.RepeatedScalarFieldContainer[str]
    themes: _containers.RepeatedScalarFieldContainer[str]
    class_: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, article_id: _Optional[int] = ..., text: _Optional[str] = ..., title: _Optional[str] = ..., date: _Optional[str] = ..., lang: _Optional[str] = ..., locations: _Optional[_Iterable[_Union[Location, _Mapping]]] = ..., semantic_vector: _Optional[_Iterable[float]] = ..., keywords: _Optional[_Iterable[str]] = ..., entities: _Optional[_Iterable[str]] = ..., themes: _Optional[_Iterable[str]] = ..., class_: _Optional[_Iterable[str]] = ...) -> None: ...

class InsertRequest(_message.Message):
    __slots__ = ["documents"]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedCompositeFieldContainer[Document]
    def __init__(self, documents: _Optional[_Iterable[_Union[Document, _Mapping]]] = ...) -> None: ...

class InsertResponse(_message.Message):
    __slots__ = ["success", "message"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...
