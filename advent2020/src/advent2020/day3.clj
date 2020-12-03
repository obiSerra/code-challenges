(ns advent2020.day1
 (:require [advent2020.utils :as utils]))

(def test-input ["..##......."
                 "#...#...#.."
                 ".#....#..#."
                 "..#.#...#.#"
                 ".#...##..#."
                 "..#.##....."
                 ".#.#.#....#"
                 ".#........#"
                 "#.##...#..."
                 "#...##....#"
                 ".#..#...#.#"])


(defn move [mr md input]
  (loop [pos [0 0]
         el-list []]
    
    (let [next-pos [(-> pos first (+ mr) (rem (count (first input))))
                    (-> pos last (+ md))]]
      (if (> (last next-pos) (count input)) el-list
          (recur next-pos (conj el-list 
                                (-> input                                    
                                    (get (last next-pos))
                                    (get (first next-pos)))))))))


(def move-silver (partial move 3 1))

(defn solve [input move-fn]
  (->> input 
       move-fn
       (remove nil?)
       (remove #(= \. %))
       count))

(def gold-moves [[1 1] [3 1] [5 1] [7 1] [1 2]])

(defn solve-gold [input moves]
  (apply * (for [mv moves]
             (solve input (partial move (first mv) (last mv))))))

(comment 
  
  (solve (utils/get-input 3) move-silver)

  (println (solve-gold (utils/get-input 3) gold-moves))

)

