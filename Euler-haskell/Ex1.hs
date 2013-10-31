import Data.List

len :: [a] -> Int

len (x:xs) = 1 + len xs
len _      = 0

mean :: [Double] -> Double
mean x = (sum x) / (fromIntegral (len x))

palindrome (x:xs) = x :(palindrome xs) ++ [x]
palindrome [] = []

isPalindrome xs = take half xs == reverse (drop ((len xs) - half) xs)
    where half = div (len xs) 2

sortByLen :: [[a]] -> [[a]]

sortByLen xs = sortBy compByLen xs
    where compByLen a b = compare (len a) (len b)
