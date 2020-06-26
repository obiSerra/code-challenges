(ns advent2019.day3
  (:require [advent2019.utils :as utils]))

;; Url
;; https://adventofcode.com/2019/day/3

(def input (utils/read-input "day3.txt"))

(def moves (map #(clojure.string/split % #",") input))

(defn get-dir [m]
  (clojure.string/replace m #"([A-Z])[0-9]*", "$1"))

(defn get-steps [m]
  (utils/to-int (clojure.string/replace m #"[A-Z]([0-9]*)", "$1")))

(defn add-steps [pos steps index sign]
  (for [x (range 1 (inc steps))] (update-in pos [index] #(sign % x))))

(defn move [pos m]
  (let [dir (get-dir m)
        steps (get-steps m)
        add-steps-pos (partial add-steps pos steps)] 
    (cond (= dir "R") (add-steps-pos 0 +) 
          (= dir "L") (add-steps-pos 0 -)
          (= dir "U") (add-steps-pos 1 +)
          (= dir "D") (add-steps-pos 1 -))))                 

(defn generate-path [wire-moves]
  (loop [pos [0 0]
         move-left wire-moves
         path []]
    (if (empty? move-left)
      path
      (let [new-path (move pos (first move-left))] 
        (recur (last new-path) (rest move-left) (concat path new-path))))))

(defn solve [moves]
  (let [first-wire (generate-path (first moves))
         second-wire (generate-path (second moves))]
    (->> (clojure.set/intersection (into #{} first-wire) (into #{} second-wire))
         (filter #(not (= % [0 0])))
         (map #(+ (Math/abs (first %)) (Math/abs (second %))) )
         (apply min))))

(comment 
  (println 
   (solve moves))
  input
  )

