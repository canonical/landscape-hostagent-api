from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
Running: InstanceState
Stopped: InstanceState

class Command(_message.Message):
    __slots__ = ["install", "set_default", "shutdown_host", "start", "stop", "uninstall"]
    class Install(_message.Message):
        __slots__ = ["cloudinit", "id"]
        CLOUDINIT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        cloudinit: str
        id: str
        def __init__(self, id: _Optional[str] = ..., cloudinit: _Optional[str] = ...) -> None: ...
    class SetDefault(_message.Message):
        __slots__ = ["id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class ShutdownHost(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class Start(_message.Message):
        __slots__ = ["id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Stop(_message.Message):
        __slots__ = ["id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Uninstall(_message.Message):
        __slots__ = ["id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    INSTALL_FIELD_NUMBER: _ClassVar[int]
    SET_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWN_HOST_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    UNINSTALL_FIELD_NUMBER: _ClassVar[int]
    install: Command.Install
    set_default: Command.SetDefault
    shutdown_host: Command.ShutdownHost
    start: Command.Start
    stop: Command.Stop
    uninstall: Command.Uninstall
    def __init__(self, start: _Optional[_Union[Command.Start, _Mapping]] = ..., stop: _Optional[_Union[Command.Stop, _Mapping]] = ..., install: _Optional[_Union[Command.Install, _Mapping]] = ..., uninstall: _Optional[_Union[Command.Uninstall, _Mapping]] = ..., set_default: _Optional[_Union[Command.SetDefault, _Mapping]] = ..., shutdown_host: _Optional[_Union[Command.ShutdownHost, _Mapping]] = ...) -> None: ...

class HostAgentInfo(_message.Message):
    __slots__ = ["hostname", "id", "instances", "token"]
    class InstanceInfo(_message.Message):
        __slots__ = ["id", "instance_state", "name", "version_id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_STATE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        instance_state: InstanceState
        name: str
        version_id: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., version_id: _Optional[str] = ..., instance_state: _Optional[_Union[InstanceState, str]] = ...) -> None: ...
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    id: str
    instances: _containers.RepeatedCompositeFieldContainer[HostAgentInfo.InstanceInfo]
    token: str
    def __init__(self, token: _Optional[str] = ..., id: _Optional[str] = ..., hostname: _Optional[str] = ..., instances: _Optional[_Iterable[_Union[HostAgentInfo.InstanceInfo, _Mapping]]] = ...) -> None: ...

class InstanceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
