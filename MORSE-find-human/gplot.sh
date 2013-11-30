#!/bin/bash

/usr/bin/gnuplot <<__EOF
set title '$2'
set datafile sep ','
set style line 1 linewidth 3
set term png
set output '$1.png'
plot '$1' u 4:1 w lines title '$3'
__EOF
