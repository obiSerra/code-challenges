(ns advent2019.day4gold
  (:require [advent2019.utils :as utils]
            [advent2019.day4 :as d4]))

;; Url
;; https://adventofcode.com/2019/day/4 -- Second part

(defn repeat? [s]
  (loop [to-check (first s)
         rem (rest s)
         cnt 0]
    (cond (and (= 1 cnt) (not= to-check (first rem))) true
          (empty? rem) false
          :else (recur (first rem) (rest rem) (if (= to-check (first rem)) (inc cnt) 0)))))

(def validate (partial d4/validate [d4/length? d4/incr? repeat?]))
(def solve (partial d4/solve validate))

(comment
  (println (solve (first d4/input) (last d4/input)))
 )
