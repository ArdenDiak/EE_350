#!/bin/bash
band_pass_filters=(1 2 3 4 5 6 7 8 9 10)

for t in ${band_pass_filters[@]}; do
    echo audioFiles/band_pass_"$t".wav
    afplay audioFiles/band_pass_"$t".wav;
    sleep 1
done
