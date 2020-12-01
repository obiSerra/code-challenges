(ns advent2020.day1
 (:require [advent2020.utils :as utils]))

(defn solve [input]
  (let [res (into [] (clojure.set/intersection (set (map #(- 2020 %) input)) (set input)))]
    (* (first res) (last res))))

(defn solve-gold [input]
  (first (for [x input
               y input
               z input
               :when (= 2020 (+ x y z))]         
           (* x y z))))

(comment 
  (println (solve (utils/get-input-int 1)))
  (println (solve-gold (utils/get-input-int 1)))
)



