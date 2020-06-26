(ns advent2019.intcodeParser
  (:require [advent2019.utils :as utils]
            [clojure.string :as s]))

;; Url
;; https://adventofcode.com/2019/day/5

(def input (first (utils/read-input "day2.txt")))

(def input-data (into [] (map utils/to-int (s/split input #","))))

(defn get-cell [program pos]
  (nth program pos))

(defn get-val [program pos]
  (nth program (get-cell program pos)))

(defn parse-operation [prog pos]
  (let [full (map utils/to-int (s/split (format "%05d" (nth prog pos)) #""))
        v (utils/to-int (apply str (drop 3 full)))]
    [(nth full 2) (second full) (first full) v]))

(defn mode-select [program pos mode]
  (if (= 0 mode) (get-val program pos) (get-cell program pos)))

(defn do-operation [op-fn program pos modes]
  (let [m-sel (partial mode-select program)
        p1 (m-sel (+ 1 pos) (nth modes 0)) 
        p2 (m-sel (+ 2 pos) (nth modes 1))
        p3 (get-cell program (+ 3 pos))]
    (update-in program [p3] (fn [_] (op-fn p1 p2)))))

(def sum-op (partial do-operation +))
(def mult-op (partial do-operation *))
