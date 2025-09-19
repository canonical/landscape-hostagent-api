from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstanceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Stopped: _ClassVar[InstanceState]
    Running: _ClassVar[InstanceState]

class CommandState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Queued: _ClassVar[CommandState]
    InProgress: _ClassVar[CommandState]
    Completed: _ClassVar[CommandState]
Stopped: InstanceState
Running: InstanceState
Queued: CommandState
InProgress: CommandState
Completed: CommandState

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HostAgentInfo(_message.Message):
    __slots__ = ("token", "uid", "hostname", "instances", "account_name", "registration_key", "default_instance_id", "unmanaged_instances")
    class InstanceInfo(_message.Message):
        __slots__ = ("id", "name", "version_id", "instance_state")
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
    DEFAULT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    UNMANAGED_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    token: str
    uid: str
    hostname: str
    instances: _containers.RepeatedCompositeFieldContainer[HostAgentInfo.InstanceInfo]
    account_name: str
    registration_key: str
    default_instance_id: str
    unmanaged_instances: _containers.RepeatedCompositeFieldContainer[HostAgentInfo.InstanceInfo]
    def __init__(self, token: _Optional[str] = ..., uid: _Optional[str] = ..., hostname: _Optional[str] = ..., instances: _Optional[_Iterable[_Union[HostAgentInfo.InstanceInfo, _Mapping]]] = ..., account_name: _Optional[str] = ..., registration_key: _Optional[str] = ..., default_instance_id: _Optional[str] = ..., unmanaged_instances: _Optional[_Iterable[_Union[HostAgentInfo.InstanceInfo, _Mapping]]] = ...) -> None: ...

class Command(_message.Message):
    __slots__ = ("assign_host", "start", "stop", "install", "uninstall", "set_default", "shutdown_host", "request_id")
    class AssignHost(_message.Message):
        __slots__ = ("uid",)
        UID_FIELD_NUMBER: _ClassVar[int]
        uid: str
        def __init__(self, uid: _Optional[str] = ...) -> None: ...
    class Start(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Stop(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Install(_message.Message):
        __slots__ = ("id", "cloudinit", "rootfsURL")
        ID_FIELD_NUMBER: _ClassVar[int]
        CLOUDINIT_FIELD_NUMBER: _ClassVar[int]
        ROOTFSURL_FIELD_NUMBER: _ClassVar[int]
        id: str
        cloudinit: str
        rootfsURL: str
        def __init__(self, id: _Optional[str] = ..., cloudinit: _Optional[str] = ..., rootfsURL: _Optional[str] = ...) -> None: ...
    class Uninstall(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class SetDefault(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class ShutdownHost(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    ASSIGN_HOST_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    INSTALL_FIELD_NUMBER: _ClassVar[int]
    UNINSTALL_FIELD_NUMBER: _ClassVar[int]
    SET_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    SHUTDOWN_HOST_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    assign_host: Command.AssignHost
    start: Command.Start
    stop: Command.Stop
    install: Command.Install
    uninstall: Command.Uninstall
    set_default: Command.SetDefault
    shutdown_host: Command.ShutdownHost
    request_id: str
    def __init__(self, assign_host: _Optional[_Union[Command.AssignHost, _Mapping]] = ..., start: _Optional[_Union[Command.Start, _Mapping]] = ..., stop: _Optional[_Union[Command.Stop, _Mapping]] = ..., install: _Optional[_Union[Command.Install, _Mapping]] = ..., uninstall: _Optional[_Union[Command.Uninstall, _Mapping]] = ..., set_default: _Optional[_Union[Command.SetDefault, _Mapping]] = ..., shutdown_host: _Optional[_Union[Command.ShutdownHost, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class CommandStatus(_message.Message):
    __slots__ = ("request_id", "command_state", "error")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    COMMAND_STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    command_state: CommandState
    error: str
    def __init__(self, request_id: _Optional[str] = ..., command_state: _Optional[_Union[CommandState, str]] = ..., error: _Optional[str] = ...) -> None: ...
