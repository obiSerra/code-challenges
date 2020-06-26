(ns advent2019.day6
  (:require [advent2019.utils :as utils]))

;; Url
;; https://adventofcode.com/2019/day/6

(def input (utils/read-input "day6.txt"))

(def input-data (map #(clojure.string/split % #"\)") input))

(defn list-nodes [graph]
  (into #{} (map second graph)))

(defn parent [graph node]
  (->> graph (filter #(= node (second %)))
       first
       first))
   
(defn orbits [graph node]
  (loop [n node
         cnt 0]
    (let [p (parent graph n)] 
      (if (nil? p)
              cnt
              (recur p (inc cnt))))))

(defn solve [graph]
  (apply + (for [x (list-nodes graph)]
     (orbits graph x))))

(comment
  (println (solve input-data))
)

