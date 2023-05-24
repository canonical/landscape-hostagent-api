# Welcome to Landscape to host agent API

[license-image]: https://img.shields.io/badge/License-MIT-blue.svg

[reference-documentation-image]: https://pkg.go.dev/badge/github.com/canonical/landscape-hostagent-api.svg
[reference-documentation-url]: https://pkg.go.dev/github.com/canonical/landscape-hostagent-api

[![License MIR][license-image]](LICENSE)
[![Go Reference documentation][reference-documentation-image]][reference-documentation-url]

This is the code repository for Landscape to host agent API, referencing the protobuf and gRPC contracts between the landscape server and host agent.

This API allows to communicates actions from Landscape to subsystems installed on a given host. You can think of VMs, containers, WSL instances… Landscape server will instruct the host agent daemon on which machines he needs up and down.

This project does provides Go and Python bindings from the reference protobuf file by autogenerating them.

## Get involved

This is an [open source](LICENSE) project and we warmly welcome community contributions, suggestions, and constructive feedback. If you're interested in contributing, please take a look at our [Contribution guidelines](CONTRIBUTING.md) first.

- to report an issue, please file a bug report against our repository, using a bug template.
- for suggestions and constructive feedback, report a feature request bug report, using the proposed template.

## Get in touch

We're friendly! We have a community forum at [https://discourse.ubuntu.com](https://discourse.ubuntu.com) where we discuss feature plans, development news, issues, updates and troubleshooting.

For news and updates, follow the [Ubuntu twitter account](https://twitter.com/ubuntu) and on [Facebook](https://www.facebook.com/ubuntu).
