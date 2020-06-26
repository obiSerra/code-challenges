(ns advent2019.day2gold
  (:require [advent2019.utils :as utils]
            [advent2019.day2 :as day2]))

;; Url
;; https://adventofcode.com/2019/day/2 -- second part

(defn find-noun-verb []
  (for [x (range 0 100)
        y (range 0 100)
        :let [res (day2/solve (-> day2/input-data
                                  (update-in [1] (fn [_] x))
                                  (update-in [2] (fn [_] y))) 0)]]
    (if (= 19690720 res)
      (+ (* 100 x) y)
      nil)))

(comment 
  (->> (find-noun-verb)
       (remove nil?)
       first))


