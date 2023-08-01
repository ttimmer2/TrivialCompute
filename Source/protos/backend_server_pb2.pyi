from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuestionResponse(_message.Message):
    __slots__ = ["Category", "QuestionType", "QuestionText"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    QUESTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    QUESTIONTEXT_FIELD_NUMBER: _ClassVar[int]
    Category: str
    QuestionType: int
    QuestionText: str
    def __init__(self, Category: _Optional[str] = ..., QuestionType: _Optional[int] = ..., QuestionText: _Optional[str] = ...) -> None: ...

class QuestionSubmission(_message.Message):
    __slots__ = ["Category", "QuestionText"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    QUESTIONTEXT_FIELD_NUMBER: _ClassVar[int]
    Category: str
    QuestionText: str
    def __init__(self, Category: _Optional[str] = ..., QuestionText: _Optional[str] = ...) -> None: ...

class QuestionRequest(_message.Message):
    __slots__ = ["Category"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    Category: str
    def __init__(self, Category: _Optional[str] = ...) -> None: ...

class SuccessMessage(_message.Message):
    __slots__ = ["Success", "MessageText"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGETEXT_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    MessageText: str
    def __init__(self, Success: bool = ..., MessageText: _Optional[str] = ...) -> None: ...

class Category(_message.Message):
    __slots__ = ["Category"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    Category: str
    def __init__(self, Category: _Optional[str] = ...) -> None: ...
