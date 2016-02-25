use <cutter_helpers.scad>;

scale = 1;
file = "default.dxf";
lip=2;
height=10;
thickness=2;
$fn=16;

add_bottom_lip(thickness,lip)2d_to_wall(thickness,height)scale([scale,scale,1])import(file=file);

