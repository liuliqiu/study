h n (x:xs) = if  mod x 3 == 0 || mod x 5 == 0 then h (n+x) xs else h n xs
h n [] = n
sumOfMultiples_3_5 n = h 0 [1..n-1]
