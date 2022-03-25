# Print Hello World
println("Hello, World!")

L = [
3 0 0 1 0 0 0 0 1 0;
0 5 3 5 4 0 0 2 6 1;
0 3 5 1 1 0 0 0 1 0;
1 5 1 13 3 1 2 3 5 1;
0 4 1 3 5 0 0 0 2 0;
0 0 0 1 0 2 0 0 0 0;
0 0 0 2 0 0 1 0 0 0;
0 2 0 3 0 0 0 6 2 0;
1 6 1 5 2 0 0 2 7 0;
0 1 0 1 0 0 0 0 0 1]

D = eigvals(L)
V = eigvecs(L)

@show D[2]
@show V[:,2]