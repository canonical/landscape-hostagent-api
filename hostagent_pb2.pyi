from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstanceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    Stopped: _ClassVar[InstanceState]
    Running: _ClassVar[InstanceState]
Stopped: InstanceState
Running: InstanceState

class HostAgentInfo(_message.Message):
    __slots__ = ["token", "uid", "hostname", "instances", "account_name", "registration_key"]
    class InstanceInfo(_message.Message):
        __slots__ = ["id", "name", "version_id", "instance_state"]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_STATE_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        version_id: str
        instance_state: InstanceState
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., version_id: _Optional[str] = ..., instance_state: _Optional[_Union[InstanceState, str]] = ...) -> None: ...
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_KEY_FIELD_NUMBER: _ClassVar[int]
    token: str
    uid: str
    hostname: str
    instances: _containers.RepeatedCompositeFieldContainer[HostAgentInfo.InstanceInfo]
    account_name: str
    registration_key: str
    def __init__(self, token: _Optional[str] = ..., uid: _Optional[str] = ..., hostname: _Optional[str] = ..., instances: _Optional[_Iterable[_Union[HostAgentInfo.InstanceInfo, _Mapping]]] = ..., account_name: _Optional[str] = ..., registration_key: _Optional[str] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ["assign_host", "start", "stop", "install", "uninstall", "set_default", "shutdown_host"]
    class AssignHost(_message.Message):
        __slots__ = ["uid"]
        UID_FIELD_NUMBER: _ClassVar[int]
        uid: str
        def __init__(self, uid: _Optional[str] = ...) -> None: ...
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
    class Install(_message.Message):
        __slots__ = ["id", "cloudinit"]
        ID_FIELD_NUMBER: _ClassVar[int]
        CLOUDINIT_FIELD_NUMBER: _ClassVar[int]
        id: str
        cloudinit: str
        def __init__(self, id: _Optional[str] = ..., cloudinit: _Optional[str] = ...) -> None: ...
    class Uninstall(_message.Message):
        __slots__ = ["id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class SetDefault(_message.Message):
        __slots__ = ["id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class ShutdownHost(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    ASSIGN_HOST_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    INSTALL_FIELD_NUMBER: _ClassVar[int]
    UNINSTALL_FIELD_NUMBER: _ClassVar[int]
    SET_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWN_HOST_FIELD_NUMBER: _ClassVar[int]
    assign_host: Command.AssignHost
    start: Command.Start
    stop: Command.Stop
    install: Command.Install
    uninstall: Command.Uninstall
    set_default: Command.SetDefault
    shutdown_host: Command.ShutdownHost
    def __init__(self, assign_host: _Optional[_Union[Command.AssignHost, _Mapping]] = ..., start: _Optional[_Union[Command.Start, _Mapping]] = ..., stop: _Optional[_Union[Command.Stop, _Mapping]] = ..., install: _Optional[_Union[Command.Install, _Mapping]] = ..., uninstall: _Optional[_Union[Command.Uninstall, _Mapping]] = ..., set_default: _Optional[_Union[Command.SetDefault, _Mapping]] = ..., shutdown_host: _Optional[_Union[Command.ShutdownHost, _Mapping]] = ...) -> None: ...
