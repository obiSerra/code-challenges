(ns advent2018.day3p2a
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

(def xxf (comp 
          (filter #(= (last %) 1))
          (map first)))

(defn free-inc [input-list]
  (->> input-list             
       (transduce xf concat)
       frequencies
       (into [])
       (transduce xxf conj)
       set))

(defn solve [ilist]
  (let [free (free-inc ilist)
        data (->> ilist
                  (transduce (map (comp 
                                   make-square 
                                   str->obj)) conj))]
    (some #(and (nil? (first (clojure.data/diff (set (:sq %)) free))) (:id %)) data)))


(->> "day3.txt"
     utils/file->lines 
     solve)
