import Data.List
import System.IO

getSidesArea :: (Int, Int, Int) -> [Int]
getSidesArea (l, w, h) = [l * w, w * h, h * l]

getRibbonVolume :: (Int, Int, Int) -> Int
getRibbonVolume (l, w, h) = l * w * h

getSmallestPerimeter :: (Int, Int, Int) -> Int
getSmallestPerimeter (l, w, h) = do
  let nums = map (2 *) $ sort [l, w, h]
  sum $ init nums

splitBy :: Char -> String -> [String]
splitBy _ "" = []
splitBy c s =
  let (l, s') = break (== c) s
   in l : case s' of
        [] -> []
        (_ : s'') -> splitBy c s''

toTriple :: [String] -> (Int, Int, Int)
toTriple [l, w, h] = (read l, read w, read h)
toTriple _ = error "This shouldn't happen"

nestedSplit :: Char -> [String] -> [(Int, Int, Int)]
nestedSplit _ [] = []
nestedSplit c (x : xs) = toTriple (splitBy c x) : nestedSplit c xs

partA :: [(Int, Int, Int)] -> Int
partA [] = 0
partA (x : xs) = do
  let nums = getSidesArea x
  sum (map (2 *) nums) + minimum nums + partA xs

partB :: [(Int, Int, Int)] -> Int
partB [] = 0
partB (x : xs) = getRibbonVolume x + getSmallestPerimeter x + partB xs

main = do
  contents <- readFile "input.txt"
  let res = nestedSplit 'x' (splitBy '\n' contents)
  print $ partA res
  print $ partB res
