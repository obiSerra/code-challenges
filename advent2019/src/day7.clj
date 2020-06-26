(ns advent2019.day7
  (:require [advent2019.utils :as utils]
            [advent2019.day5 :as d5]
            [advent2019.day5gold :as d5gold]
            [advent2019.intcodeParser :as parser]))

;; Url
;; https://adventofcode.com/2019/day/7

(def input (first (utils/read-input "day7.txt")))

(def input-data (into [] (map utils/to-int (clojure.string/split input #","))))

(defn run-program [program input1 input2]
  (loop [prg program
         pos 0
         out nil
         in [input1 input2]]
    (let [[m1 m2 m3 op] (parser/parse-operation prg pos)
          modes [m1 m2 m3]]
      (cond (= 1 op) (recur (parser/sum-op prg pos modes) (+ 4 pos) out in)
            (= 2 op) (recur (parser/mult-op prg pos modes) (+ 4 pos) out in)
            (= 3 op) (recur (d5/input-op prg pos (first in)) (+ 2 pos) out (rest in))
            (= 4 op) (recur prg (+ pos 2) (d5/output-op m1 prg pos) in)
            (= 5 op) (recur prg (d5gold/jump-if-true prg pos modes) out in)
            (= 6 op) (recur prg (d5gold/jump-if-false prg pos modes) out in)
            (= 7 op) (recur (d5gold/less-than prg pos modes) (+ pos 4) out in)
            (= 8 op) (recur (d5gold/equals-op prg pos modes) (+ pos 4) out in)           
            (= 99 op) out
            :else ["error" op]))))

(defn solve [program]
  (apply max (for [xa (range 0 5)
                   xb (range 0 5)
                   xc (range 0 5)
                   xd (range 0 5)
                   xe (range 0 5)
                   :when (= 5 (count (into #{} [xa xb xc xd xe])))]
               (->> 0
                    (run-program program xa)
                    (run-program program xb)
                    (run-program program xc)
                    (run-program program xd)
                    (run-program program xe)))))

(comment
  (println (solve input-data))  
)









