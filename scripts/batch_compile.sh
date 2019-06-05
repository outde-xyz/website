#!/bin/sh

# use this script to automatically compile tikz figures to svgs

scale=2

# compile to pdf
for source in *.tex; do
    latexmk -pdf -g $source
done

# clean up tex files
latexmk -c

# convert pdf to svg with same filename
for img in *.pdf; do
    pdf2svg $img $(basename $i .pdf)
done

# scale each svg
for img in *.svg; do
    width_cur=$(grep -ioP -m 1 '(?<=width=")[0-9.]*(?=pt")' $img)
    height_cur=$(grep -ioP -m 1 '(?<=height=")[0-9.]*(?=pt")' $img)

    width_new=$(echo "$scale * $width_cur" | bc -l)
    height_new=$(echo "$scale * $height_cur" | bc -l)

    sed -i "s/$width_cur/$width_new/g" $img
    sed -i "s/$height_cur/$height_new/g" $img
done
