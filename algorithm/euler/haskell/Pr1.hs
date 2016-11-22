
h n x y = if x >= y then n else if mod x 3 == 0 || mod x 5 == 0 then h (n + x) (x + 1) y else h n (x + 1) y
f n = h 0 1 (n - 1)

