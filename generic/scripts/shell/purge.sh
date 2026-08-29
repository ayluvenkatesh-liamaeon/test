#!/usr/bin/env bash

# Purge .log files older than N days in a given directory.
# Usage: ./purge.sh <path> <days>

set -eu

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <path> <days>" >&2
  exit 1
fi

TARGET_DIR="$1"
DAYS="$2"

if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: Directory not found: $TARGET_DIR" >&2
  exit 1
fi

if ! [[ "$DAYS" =~ ^[0-9]+$ ]]; then
  echo "Error: Days must be a non-negative integer." >&2
  exit 1
fi

find "$TARGET_DIR" -type f -name "*.log" -mtime +"$DAYS" -delete

echo "Purged .log files older than $DAYS day(s) in $TARGET_DIR"
