h = 0.05;
//+
Point(1) = {-0.5, -0.5, 0, h};
//+
Point(3) = {1, -0.5, 0, h};
//+
Point(4) = {1, 1.5, 0, h};
//+
Point(5) = {-0.5, 1.5, 0, h};
//+
Line(1) = {1, 3};
//+
Line(2) = {3, 4};
//+
Line(3) = {4, 5};
//+
Line(4) = {5, 1};
//+
Curve Loop(1) = {1, 2, 3, 4};
//+
Plane Surface(1) = {1};
//+
Physical Curve("Gamma") = {1, 2, 3, 4};
//+
Physical Surface("Omega") = {1};
