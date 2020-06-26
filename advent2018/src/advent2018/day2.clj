(ns advent2018.day2
  (:require [advent2018.utils :as utils]))

;; Solved

(def ex ["abcdef"
         "bababc"
         "abbcde"
         "abcccd"
         "aabcdd"
         "abcdee"
         "ababab"])

(defn r-gropus [els]
  [(if (some #(= 2 (last %)) els) 1 0)
   (if (some #(= 3 (last %)) els) 1 0)])

(defn count-letters [str]
  (r-gropus (frequencies str)))


(defn r-sum [acc v] [(+ (first acc) (first v))
                     (+ (last acc) (last v))])

(let [vals (reduce r-sum (map count-letters (utils/file->lines "day2.txt")))]
  (* (first vals)
     (second vals)))
