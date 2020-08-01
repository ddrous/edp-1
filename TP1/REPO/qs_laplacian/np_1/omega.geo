h = 0.05;
//+
Point(1) = {0, 0, 0, h};
//+
Point(2) = {1, 0, 0, h};
//+
Point(3) = {-1, 0, 0, h};
//+
Point(4) = {0, 1, 0, h};
//+
Circle(1) = {2, 1, 4};
//+
Circle(2) = {4, 1, 3};
//+
Circle(3) = {3, 1, 2};
//+
Physical Curve("Dirichlet") = {1};
//+
Physical Curve("Neumann") = {2};
//+
Physical Curve("Robin") = {3};
//+
Curve Loop(1) = {2, 3, 1};
//+
Plane Surface(1) = {1};
//+
Physical Surface("Omega") = {1};
