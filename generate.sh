#!/bin/bash

# generate python
protoc -I=. --python_out=generated main.proto
protoc -I=. --python_out=generated hardwareMessages.proto
protoc -I=. --python_out=generated simulationMessages.proto

# generate csharp
protoc -I=. --csharp_out=generated main.proto
protoc -I=. --csharp_out=generated hardwareMessages.proto
protoc -I=. --csharp_out=generated simulationMessages.proto
