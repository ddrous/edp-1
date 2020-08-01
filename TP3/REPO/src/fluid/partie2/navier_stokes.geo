h = 0.05;
//+
Point(1) = {0, 0, 0, h};
//+
Point(2) = {5, 0, 0, h};
//+
Point(3) = {5, 1, 0, h};
//+
Point(4) = {0, 1, 0, h};
//+
Point(5) = {0.4, 0.4, 0, h};
//+
Point(6) = {0.6, 0.4, 0, h};
//+
Point(7) = {0.6, 0.6, 0, h};
//+
Point(8) = {0.4, 0.6, 0, h};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 1};
//+
Line(5) = {5, 6};
//+
Line(6) = {6, 7};
//+
Line(7) = {7, 8};
//+
Line(8) = {8, 5};
//+
Physical Curve("Gamma_in") = {4};
//+
Physical Curve("Gamma_out") = {2};
//+
Physical Curve("Gamma_0_1") = {1, 3};
//+
Physical Curve("Gamma_0_2") = {5, 6, 7, 8};
//+
Curve Loop(1) = {1, 2, 3, 4};
//+
Curve Loop(2) = {6, 7, 8, 5};
//+
Plane Surface(1) = {1, 2};
//+
Physical Surface("Omega") = {1};
