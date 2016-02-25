module 2d_to_wall(thickness=2,height=10){
    difference(){
        minkowski(){
            linear_extrude(height=height/2,center=true)children();
            cylinder(r=thickness,height/2,center=true);
        }
        linear_extrude(height=height*2,center=true)children();
    }
}
module add_bottom_lip(thickness=2,lip=2){
    union(){
        children();
        difference(){
            minkowski(){
                cylinder(r=lip,thickness);
                children();
            }
            translate([0,0,thickness])minkowski(){
                cylinder(r=lip*2,thickness);
                children();
            }
        }
    }
}
