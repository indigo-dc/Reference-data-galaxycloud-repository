#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "List file: $line"
    wget $line
done < "$1"
