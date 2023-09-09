#!/usr/bin/env bash

set -xe

find . -type f -name "*.py" -exec python3 {} \;
