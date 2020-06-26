(ns advent2018.day3
  (:require [advent2018.utils :as utils]
            [clojure.string :as string]))

;; Solved

(def ex ["#1 @ 1,3: 4x4"
         "#2 @ 3,1: 4x4"
         "#3 @ 5,5: 2x2"])


(def parse-row  (comp
                 read-string
                 #(string/replace % #"#" "")
                 #(string/replace % #" " "")))

(defn split-row [val-str]
  (let [vals (map parse-row (string/split val-str #"(:|@|,|x)"))]
    {:id (first vals)
     :left (nth vals 1)
     :top (nth vals 2)
     :w (nth vals 3)
     :h (nth vals 4)
     :rest vals}))

(defn make-square [sq-obj]
  (assoc sq-obj :sq
         (for [x (range (:w sq-obj))
               y (range (:h sq-obj))]
           [(+ (:left sq-obj) x) (+ (:top sq-obj) y)])))

(defn str->obj [val-str]
  (->> val-str
       split-row))

(def xf (map (comp
              :sq
              make-square
              str->obj)))

(defn solve [input-list]
  (->> input-list
       (transduce xf concat)
       frequencies
       (into [])
       (filter #(>= (last %) 2))
       count))

;; (solve ex)

(println (->> "day3.txt"
              utils/file->lines
              solve))
