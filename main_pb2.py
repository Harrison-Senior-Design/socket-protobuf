# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import beltMessages_pb2 as beltMessages__pb2
import unityMessages_pb2 as unityMessages__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='main.proto',
  package='main',
  syntax='proto3',
  serialized_options=_b('\252\002\024Biofeedback.Protobuf'),
  serialized_pb=_b('\n\nmain.proto\x12\x04main\x1a\x12\x62\x65ltMessages.proto\x1a\x13unityMessages.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x84\x01\n\x07Wrapper\x12#\n\x06opcode\x18\x01 \x01(\x0e\x32\x13.main.OperationCode\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12%\n\x07payload\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any*;\n\rOperationCode\x12\x0e\n\nANGLE_DATA\x10\x00\x12\x1a\n\x16MOVE_STARTING_LOCATION\x10\x01\x42\x17\xaa\x02\x14\x42iofeedback.Protobufb\x06proto3')
  ,
  dependencies=[beltMessages__pb2.DESCRIPTOR,unityMessages__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_OPERATIONCODE = _descriptor.EnumDescriptor(
  name='OperationCode',
  full_name='main.OperationCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANGLE_DATA', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_STARTING_LOCATION', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=256,
  serialized_end=315,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONCODE)

OperationCode = enum_type_wrapper.EnumTypeWrapper(_OPERATIONCODE)
ANGLE_DATA = 0
MOVE_STARTING_LOCATION = 1



_WRAPPER = _descriptor.Descriptor(
  name='Wrapper',
  full_name='main.Wrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opcode', full_name='main.Wrapper.opcode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='main.Wrapper.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='main.Wrapper.payload', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=254,
)

_WRAPPER.fields_by_name['opcode'].enum_type = _OPERATIONCODE
_WRAPPER.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_WRAPPER.fields_by_name['payload'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['Wrapper'] = _WRAPPER
DESCRIPTOR.enum_types_by_name['OperationCode'] = _OPERATIONCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Wrapper = _reflection.GeneratedProtocolMessageType('Wrapper', (_message.Message,), dict(
  DESCRIPTOR = _WRAPPER,
  __module__ = 'main_pb2'
  # @@protoc_insertion_point(class_scope:main.Wrapper)
  ))
_sym_db.RegisterMessage(Wrapper)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
