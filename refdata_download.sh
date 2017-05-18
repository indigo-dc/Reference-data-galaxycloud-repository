#!/bin/bash

cvmfs_dir="/cvmfs"
repo_dir="elixir-italy.galaxy.refdata"

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo "List file: $line"
    python refdata_download.py -i 'lists/'$line -o $cvmfs_dir -s $repo_dir
done < "$1"
