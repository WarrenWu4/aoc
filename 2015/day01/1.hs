import System.IO

partA :: Int -> String -> Int
partA a [] = a
partA a (x:xs)
  | x == '(' = partA (a+1) xs
  | x == ')' = partA (a-1) xs
  | otherwise = partA a xs

partB :: Int -> Int -> String -> Int
partB a b [] = b
partB a b (x:xs)
  | x == '(' = partB (a+1) (b+1) xs
  | x == ')' = if (a-1) == - 1 then b+1 else partB (a-1) (b+1) xs
  | otherwise = partB a b xs

main :: IO ()
main = do
  contents <- readFile "input.txt"
  let ansA = partA 0 contents
  print ansA 
  let ansB = partB 0 0 contents
  print ansB
