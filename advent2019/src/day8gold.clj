(ns advent2019.day8gold
  (:require [advent2019.utils :as utils]
            [advent2019.day8 :as d8]))

;; Url
;; https://adventofcode.com/2019/day/8 -- second part

(defn solve [w h data]
  (let [colored (map #(cond (= % "0") " " 
                            (= % "2") nil 
                            :else "I") data)
        pixels (apply map (fn [& vs] vs) (partition (* h w) colored))]
    (->> pixels
         (map #(first (filter (comp not nil?) %)))
         (partition w))))

(comment 
  (map println (solve 25 6 d8/input-data)))







