(ns advent2019.day6gold
  (:require [advent2019.utils :as utils]
            [advent2019.day6 :as day6]))

;; Url
;; https://adventofcode.com/2019/day/6 -- second part

(defn orbits [graph node]
  (loop [n node
         orbits []]
    (let [p (day6/parent graph n)] 
      (if (nil? p)
              orbits
              (recur p (conj orbits p))))))

(defn solve [graph node1 node2]
  (let [orbs1 (orbits graph node1)
        orbs2 (orbits graph node2)
        common (first (filter #(>= (.indexOf orbs2 %) 0) orbs1))] 
    (if (nil? common)
      false
      (+ (.indexOf orbs1 common) (.indexOf orbs2 common)))))

(comment
  (println (solve day6/input-data "YOU" "SAN"))
)

