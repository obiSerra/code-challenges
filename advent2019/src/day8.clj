(ns advent2019.day8
  (:require [advent2019.utils :as utils]))

;; Url
;; https://adventofcode.com/2019/day/8

(def input (first (utils/read-input "day8.txt")) )

(def input-data (clojure.string/split input #""))

(def size [25 6])

(defn solve [width height input-data]
  (let [layers (partition height (partition width input-data))]
    (let [nums (frequencies 
                (apply concat 
                       (last (reduce (fn [acc v]
                                       (if (or (nil? acc) (< (or (first v) 0) (or (first acc) 0))) v acc)) 
                                     (map (fn [v] [(get (frequencies (apply concat v)) "0") v]) layers)))))]
      (* (get nums "1") (get nums "2")))))

(comment 
  (println (solve (first size) (second size) input-data)))



