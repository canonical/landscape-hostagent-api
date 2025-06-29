#!/usr/bin/env sh
set -eu

HOSTAGENT_API_DIR=${HOSTAGENT_API_DIR:-.}

go get google.golang.org/grpc

go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest

export PATH="$(go env GOPATH)/bin:$PATH"


protoc --proto_path="$HOSTAGENT_API_DIR" \
    --go_out="$HOSTAGENT_API_DIR" \
    --go_opt=paths=source_relative \
    --go-grpc_out="$HOSTAGENT_API_DIR" \
    --go-grpc_opt=paths=source_relative \
    --experimental_allow_proto3_optional \
    "$HOSTAGENT_API_DIR/hostagent.proto"

~/.local/share/pipx/venvs/grpcio-tools/bin/python -m grpc_tools.protoc \
    -I"$HOSTAGENT_API_DIR" \
    --python_out="$HOSTAGENT_API_DIR" \
    --pyi_out="$HOSTAGENT_API_DIR" \
    --grpc_python_out="$HOSTAGENT_API_DIR" \
    --experimental_allow_proto3_optional \
    "$HOSTAGENT_API_DIR/hostagent.proto"

echo "Done!"
