#!/bin/sh

# use this script to automatically compile tikz figures to svgs

scale=2
converter="pdf2svg"

# compile to pdf
for source in *.tex; do
    latexmk -pdf -g -quiet "$source"
done

# clean up tex files
latexmk -c

# convert pdf to svg with same filename
for img in *.pdf; do
    svg=$(basename "$img" .pdf).svg
    if [ "$converter" = "pdf2svg" ]; then
        pdf2svg "$img" "$svg"
    elif [ "$converter" = "inkscape" ]; then
        inkscape -z -f "$img" -l "$svg"
    fi
done

# scale each svg
if [ "$converter" = "pdf2svg" ]; then
    for img in *.svg; do
        width_cur=$(grep -ioP -m 1 '(?<=width=")[0-9.]*(?=pt")' "$img")
        height_cur=$(grep -ioP -m 1 '(?<=height=")[0-9.]*(?=pt")' "$img")

        width_new=$(echo "$scale * $width_cur" | bc -l)
        height_new=$(echo "$scale * $height_cur" | bc -l)

        sed -i "s/${width_cur}pt/${width_new}pt/" "$img"
        sed -i "s/${height_cur}pt/${height_new}pt/" "$img"
    done
fi

# clean up pdfs
for source in *.tex; do
    pdf=$(basename "$source" .tex).pdf
    rm "$pdf"
done
