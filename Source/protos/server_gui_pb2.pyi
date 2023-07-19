from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    A: _ClassVar[ResponseType]
    B: _ClassVar[ResponseType]
    C: _ClassVar[ResponseType]
A: ResponseType
B: ResponseType
C: ResponseType

class RequestQuestion(_message.Message):
    __slots__ = ["Player"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    Player: int
    def __init__(self, Player: _Optional[int] = ...) -> None: ...

class RollDiceMessage(_message.Message):
    __slots__ = ["Player", "Location"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    Player: int
    Location: int
    def __init__(self, Player: _Optional[int] = ..., Location: _Optional[int] = ...) -> None: ...

class ValidSpotMessage(_message.Message):
    __slots__ = ["ValidSpot"]
    VALIDSPOT_FIELD_NUMBER: _ClassVar[int]
    ValidSpot: str
    def __init__(self, ValidSpot: _Optional[str] = ...) -> None: ...

class NewSpotMessage(_message.Message):
    __slots__ = ["Player", "Spot"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    SPOT_FIELD_NUMBER: _ClassVar[int]
    Player: int
    Spot: int
    def __init__(self, Player: _Optional[int] = ..., Spot: _Optional[int] = ...) -> None: ...

class NewSpotActionOrMessage(_message.Message):
    __slots__ = ["Player", "RT"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    RT_FIELD_NUMBER: _ClassVar[int]
    Player: int
    RT: int
    def __init__(self, Player: _Optional[int] = ..., RT: _Optional[int] = ...) -> None: ...

class CategoryFromGUI(_message.Message):
    __slots__ = ["CategoryName"]
    CATEGORYNAME_FIELD_NUMBER: _ClassVar[int]
    CategoryName: str
    def __init__(self, CategoryName: _Optional[str] = ...) -> None: ...

class QuestionGS(_message.Message):
    __slots__ = ["CategoryType", "Question"]
    CATEGORYTYPE_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    CategoryType: str
    Question: str
    def __init__(self, CategoryType: _Optional[str] = ..., Question: _Optional[str] = ...) -> None: ...

class SuccessMessageGS(_message.Message):
    __slots__ = ["Success", "messageText"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGETEXT_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    messageText: str
    def __init__(self, Success: bool = ..., messageText: _Optional[str] = ...) -> None: ...

class ResponseSuccess(_message.Message):
    __slots__ = ["player", "success"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    player: int
    success: bool
    def __init__(self, player: _Optional[int] = ..., success: bool = ...) -> None: ...

class UpdatePlayerScoreMessage(_message.Message):
    __slots__ = ["player", "Category", "answered"]
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ANSWERED_FIELD_NUMBER: _ClassVar[int]
    player: int
    Category: int
    answered: bool
    def __init__(self, player: _Optional[int] = ..., Category: _Optional[int] = ..., answered: bool = ...) -> None: ...
