(ns advent2019.day1
  (:require [advent2019.utils :as utils]))

;; Url
;; https://adventofcode.com/2019/day/1

(def input-file "day1-1.txt")

(def input-data (map utils/to-int (utils/read-input input-file)))

(defn calc-fuel [mass]
  (- (int (Math/floor (/ mass 3))) 2))

(defn solve []
    (reduce + (map calc-fuel input-data)))


(comment
  (println (solve)))
