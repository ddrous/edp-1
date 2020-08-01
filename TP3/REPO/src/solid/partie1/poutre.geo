// Gmsh project created on Sat Apr 18 15:19:28 2020
h = 0.2;
L = 8;
//+
Point(1) = {0, 0, 0, h};
//+
Point(2) = {L, 0, 0, h};
//+
Point(3) = {L, 1, 0, h};
//+
Point(4) = {0, 1, 0, h};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Curve Loop(1) = {4, 1, 2, 3};
//+
Plane Surface(1) = {1};
//+
Physical Curve("Gamma1") = {1};
//+
Physical Curve("Gamma2") = {2};
//+
Physical Curve("Gamma3") = {3};
//+
Physical Curve("Gamma4") = {4};
//+
Physical Surface("Omega") = {1};
