#!/bin/bash

# generate python
protoc --python_out=generated main.proto hardwareMessages.proto simulationMessages.proto

# generate csharp
protoc --csharp_out=generated main.proto hardwareMessages.proto simulationMessages.proto
