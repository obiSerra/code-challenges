(ns advent2018.day5Home
  (:require [advent2018.utils :as utils]))

;; Solved

(def ex "dabAcCaCBAcCcaDA")

(def in (butlast (clojure.string/split (utils/read-input "day5.txt") #"")) )

(defn simplify 
  ([letters] letters)
  ([letters val] 
   (if (and (not (empty? letters))        
            (= (clojure.string/lower-case (last letters)) 
               (clojure.string/lower-case val))
        (not (= (last letters) val)))
     (if (empty? letters) [] (vec (butlast letters)))
     (conj letters val))))



(defn solve [data] 
  (reduce simplify [] data))

((comp
  count
  solve) in)
