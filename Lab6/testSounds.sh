#!/bin/bash
for audiofile in audioFiles/*.wav; do
    echo "$audiofile"
    afplay "$audiofile"
    sleep 1
done
