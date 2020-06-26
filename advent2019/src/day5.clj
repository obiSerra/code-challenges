(ns advent2019.day5
  (:require [advent2019.utils :as utils]
            [advent2019.intcodeParser :as parser]))

;; Url
;; https://adventofcode.com/2019/day/5

(def input (first (utils/read-input "day5.txt")))

(def input-data (into [] (map utils/to-int (clojure.string/split input #","))))

(defn input-op [program pos value]
  (assoc-in program [(parser/get-cell program (+ 1 pos))] value))

(defn output-op [mode program pos]
  (parser/mode-select program (+ 1 pos) mode))

(defn solve [program position]
  (loop [prg program
         pos position
         out nil]
    (let [[m1 m2 m3 op] (parser/parse-operation prg pos)
          modes [m1 m2 m3]]
      (cond (= 1 op) (recur (parser/sum-op prg pos modes) (+ 4 pos) out)
            (= 2 op) (recur (parser/mult-op prg pos modes) (+ 4 pos) out)
            (= 3 op) (recur (input-op prg pos 1) (+ 2 pos) out)
            (= 4 op) (if (= 0 (output-op m1 prg pos)) 
                       (recur prg (+ pos 2) out) 
                       (recur prg (+ pos 2) (conj out (output-op m1 prg pos))))
            (or (= 99 op) (> pos (count prg))) out))))

(comment
  (println (solve input-data 0))
)
  

