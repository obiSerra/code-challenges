(ns advent2018.day2
  (:require [advent2018.utils :as utils]))

;; Solved

(defn check-diff [to-check ref]
  (loop [remaining (clojure.string/split to-check #"")
         ref-rem (clojure.string/split ref #"")
         common []]
    (if (empty? remaining)
      (if (empty? common) nil common)
      (recur (rest remaining)
             (rest ref-rem)
             (if (= (first remaining) (first ref-rem))
               (conj common (first remaining))
               common)))))

(defn get-difference [str-list]
  (for [x str-list
        y str-list
        :let [d (check-diff x y)]]

    (if (= 1 (- (count x) (count d)))
      d
      nil)))

(->> "day2.txt"
     utils/file->lines
     get-difference
     (remove nil?)
     first
     (apply str))

;; (println (apply str (first (remove nil? (get-difference (utils/file->lines "day2.txt"))))))
