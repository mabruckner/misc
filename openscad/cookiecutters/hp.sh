#!/usr/bin/bash
# lightning bolt cutters in 1" and 1 1/4"
# star cutters in 1/2" and 1/4"
mkdir output
openscad -o output/star_small.stl -D'file="star.dxf"' -Dscale=6.35 -Dthickness=1 -Dlip=1 make_cutter.scad
openscad -o output/star_big.stl -D'file="star.dxf"' -Dscale=12.7 -Dthickness=1 -Dlip=1 make_cutter.scad
openscad -o output/lightning_small.stl -D'file="lightning.dxf"' -Dscale=25.4 -Dthickness=1 -Dlip=1 make_cutter.scad
openscad -o output/lightning_big.stl -D'file="lightning.dxf"' -Dscale=31.75 -Dthickness=1 -Dlip=1 make_cutter.scad
