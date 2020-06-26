(ns advent2019.day5gold
  (:require [advent2019.utils :as utils]
            [advent2019.day5 :as d5]
            [advent2019.intcodeParser :as parser]))

;; Url
;; https://adventofcode.com/2019/day/5 -- second part

(def input (first (utils/read-input "day5.txt")))

(def input-data (into [] (map utils/to-int (clojure.string/split input #","))))

(defn jump-if [pred program pos modes]
  (if (pred 0 (parser/mode-select program (+ 1 pos) (first modes)))
    (parser/mode-select program (+ 2 pos) (second modes))
    (+ 3 pos)))

(def jump-if-true (partial jump-if not=))
(def jump-if-false (partial jump-if =))

(defn compare-op [pred program pos modes]
  (let [sel (partial parser/mode-select program)
        p1 (sel (+ 1 pos) (first modes))
        p2 (sel (+ 2 pos) (second modes))
        p3 (parser/get-cell program (+ 3 pos))
        v (if (pred p1 p2) 1 0)]
    (assoc-in program [p3] v)))

(def less-than (partial compare-op <))
(def equals-op (partial compare-op =))

(defn solve [program id]
  (loop [prg program
         pos 0
         out []]
    (let [[m1 m2 m3 op] (parser/parse-operation prg pos)
          modes [m1 m2 m3]]
      (cond (= 1 op) (recur (parser/sum-op prg pos modes) (+ 4 pos) out)
            (= 2 op) (recur (parser/mult-op prg pos modes) (+ 4 pos) out)
            (= 3 op) (recur (d5/input-op prg pos id) (+ 2 pos) out)
            (= 4 op) (recur prg (+ pos 2) (conj out (d5/output-op m1 prg pos)))
            (= 5 op) (recur prg (jump-if-true prg pos modes) out)
            (= 6 op) (recur prg (jump-if-false prg pos modes) out)
            (= 7 op) (recur (less-than prg pos modes) (+ pos 4) out)
            (= 8 op) (recur (equals-op prg pos modes) (+ pos 4) out)           
            (= 99 op) out
            :else ["error" op]))))

(comment
  (println (solve input-data 5))  
)
  



