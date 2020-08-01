h = 0.05;
//+
Point(1) = {-0, -0, 0, h};
//+
Point(2) = {1, -0, 0, h};
//+
Point(3) = {-1, 0, 0, h};
//+
Point(4) = {0, -1, 0, h};
//+
Circle(1) = {2, 1, 3};
//+
Circle(2) = {3, 1, 4};
//+
Line(3) = {1, 2};
//+
Line(4) = {1, 4};
//+
Curve Loop(1) = {1, 2, -4, 3};
//+
Plane Surface(1) = {1};
//+
Physical Curve("Dirichlet") = {3, 1, 2, 4};
//+
Physical Surface("Omega") = {1};
