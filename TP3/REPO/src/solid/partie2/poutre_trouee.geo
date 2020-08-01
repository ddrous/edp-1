// Gmsh project created on Sat Apr 18 15:19:28 2020
h = 0.1;
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
Point(5) = {2, 0.5, 0, h};
//+
Point(6) = {2.3, 0.5, 0, h};
//+
Point(7) = {1.7, 0.5, 0, h};
//+
Point(8) = {6, 0.5, 0, h};
//+
Point(9) = {6.3, 0.5, 0, h};
//+
Point(10) = {5.7, 0.5, 0, h};
//+
Circle(5) = {6, 5, 7};
//+
Circle(6) = {7, 5, 6};
//+
Circle(7) = {9, 8, 10};
//+
Circle(8) = {10, 8, 9};
//+
Curve Loop(2) = {6, 5};
//+
Curve Loop(3) = {8, 7};
//+
Plane Surface(1) = {1, 2, 3};
//+
Physical Curve("Gamma1") = {1};
//+
Physical Curve("Gamma2") = {2};
//+
Physical Curve("Gamma3") = {3};
//+
Physical Curve("Gamma4") = {4};
//+
Physical Curve("Trou1") = {6, 5};
//+
Physical Curve("Trou2") = {8, 7};
//+
Physical Surface("Omega") = {1};
