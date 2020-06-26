(ns advent2019.day7gold
  (:require [advent2019.utils :as utils]
            [advent2019.day5 :as d5]
            [advent2019.day5gold :as d5gold]
            [advent2019.day7 :as d7]
            [advent2019.intcodeParser :as parser]))

;; Url
;; https://adventofcode.com/2019/day/7 -- second part

(def input (first (utils/read-input "day7.txt")))

(def input-data (into [] (map utils/to-int (clojure.string/split input #","))))

(defn run-program [program ps & inputs]
  (loop [prg program
         pos ps
         out []
         in inputs]
    (let [[m1 m2 m3 op] (parser/parse-operation prg pos)
          modes [m1 m2 m3]]
      (cond (= 1 op) (recur (parser/sum-op prg pos modes) (+ 4 pos) out in)
            (= 2 op) (recur (parser/mult-op prg pos modes) (+ 4 pos) out in)
            (= 3 op) (recur (d5/input-op prg pos (first in)) (+ 2 pos) out (rest in))
            (= 4 op) [(d5/output-op m1 prg pos) (+ 2 pos) prg]
            (= 5 op) (recur prg (d5gold/jump-if-true prg pos modes) out in)
            (= 6 op) (recur prg (d5gold/jump-if-false prg pos modes) out in)
            (= 7 op) (recur (d5gold/less-than prg pos modes) (+ pos 4) out in)
            (= 8 op) (recur (d5gold/equals-op prg pos modes) (+ pos 4) out in)
            (= 99 op) out
            :else ["error" op]))))

(defn solve-program [program s]
  (loop [run 0
         states (into [] (concat [(run-program program 0 (first s) 0)] (take 4 (repeat nil)) ))]

    (let [nxt (rem (inc run) (count states))
          prv (if (= 0 run) (- (count states) 1) (- run 1))] 
      (cond (every? empty? (butlast states)) (first (last states))          
            :else (recur nxt
                         (update-in states [nxt] (fn [_] (if (nil? (nth states nxt)) 
                                                           (run-program program 0 (nth s nxt) (first (nth states run)))
                                                           (run-program (nth (nth states nxt) 2) (second (nth states nxt)) (first (nth states run)))))))))))

(defn solve [program]
  (apply max (for [xa (range 5 10)
                   xb (range 5 10)
                   xc (range 5 10)
                   xd (range 5 10)
                   xe (range 5 10)
                   :when (= 5 (count (into #{} [xa xb xc xd xe])))]
               (solve-program input-data [xa xb xc xd xe]))))

(comment
  (println (solve input-data))
)

