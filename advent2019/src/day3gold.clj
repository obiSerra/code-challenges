(ns advent2019.day3gold
  (:require [advent2019.utils :as utils]
            [advent2019.day3 :as day3]))

;; Url
;; https://adventofcode.com/2019/day/3 -- second part

(defn solve [moves]
  (let [first-wire (day3/generate-path (first moves))
         second-wire (day3/generate-path (second moves))]

    (->> (clojure.set/intersection (into #{} first-wire) (into #{} second-wire))
         (filter #(not (= % [0 0])))
         (map #(+ 2 (.indexOf first-wire %) (.indexOf second-wire %)))
         (apply min))))

(comment 
  (solve day3/moves))



