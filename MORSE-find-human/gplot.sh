#!/bin/bash

/usr/bin/gnuplot <<__EOF
set title '$2'
set xlabel "Time in seconds"
set ylabel "Position in meters"
set datafile sep ','
set style line 1 linewidth 3
set term png
set output '$WORKSPACE/$FSMTRA.png'
plot '$1' u 4:1 w lines title '$3'
__EOF
