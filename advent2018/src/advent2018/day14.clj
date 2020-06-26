(ns advent2018.day14
  (:require [advent2018.utils :as utils]
            [clojure.string :as s]))

(def pos (atom [0 1]))

(def starting-board [3 7])

(defn new-board [board]
  (concat board (map read-string (s/split (str (apply + board)) #""))))

(defn move-player [p r l]
  (swap! pos #(mod (+ (nth % p) r) l)))

(defn round [board]


)

(new-board starting-board)
