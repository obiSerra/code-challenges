(ns advent2019.day2
  (:require [advent2019.utils :as utils]
            [advent2019.intcodeParser :as parser]))

;; Url
;; https://adventofcode.com/2019/day/2

(def input (first (utils/read-input "day2.txt")))

(def input-data (into [] (map utils/to-int (clojure.string/split input #","))))

(defn solve [program position]
  (loop [prg program
         pos position] 
    (let [[m1 m2 m3 op] (parser/parse-operation prg pos)
          modes [m1 m2 m3]]
      
      (cond (= 1 op) (recur (parser/sum-op prg pos modes) (+ 4 pos))
            (= 2 op) (recur (parser/mult-op prg pos modes) (+ 4 pos))
            (= 99 op) (first prg)))))


(comment 
  (= 3716293 (intcode-parser handlers (-> input-data
                                          (update-in [1] (fn [_] 12))
                                          (update-in [2] (fn [_] 2))) 0))
  
  (solve (-> input-data
             (update-in [1] (fn [_] 12))
             (update-in [2] (fn [_] 2))) 0))
