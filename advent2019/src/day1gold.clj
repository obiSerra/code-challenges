(ns advent2019.day1gold
  (:require [advent2019.utils :as utils]
            [advent2019.day1 :as d1]))

;; Url
;; https://adventofcode.com/2019/day/1 -- second part


(defn calc-fuel-rec [mass]
  (loop [rem (d1/calc-fuel mass)
         tot (d1/calc-fuel mass)]
    (if (>= 0 rem)
      tot
      (recur (max (d1/calc-fuel rem) 0) (+ tot (max (d1/calc-fuel rem) 0))))))

(defn solve []
    (reduce + (map calc-fuel-rec d1/input-data)))

(comment
  (println (solve)))
