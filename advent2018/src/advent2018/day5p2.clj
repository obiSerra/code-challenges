(ns advent2018.day5p2
  (:require [advent2018.utils :as utils]))

(def ex "dabAcCaCBAcCcaDA")

(def in (butlast (clojure.string/split 
                  (utils/read-input "day5.txt")
                  #"")))


;; (def unq (set (map clojure.string/lower-case (set in))))

(defn simplify 
  ([letters] letters)
  ([letters val] 
   (if (and (not (empty? letters))        
            (= (clojure.string/lower-case (last letters)) 
               (clojure.string/lower-case val))
        (not (= (last letters) val)))
     (if (empty? letters) [] (vec (butlast letters)))
     (conj letters val))))

(def tick (atom 0))

(defn red-lists
  ([acc] acc)
  ([old-v new-v]
   (if (< old-v (count new-v))
     old-v
     (count new-v))))

(defn xxf [data]
  (comp 
   ;; (map (fn [v] (identity data)))
   (map #(clojure.string/replace (clojure.string/join "" data) (re-pattern (str "(?i)" %)) ""))
   ))

(defn solve [data]
  (let [unq (set (map clojure.string/lower-case (set data)))
        tc (transduce (xxf data) conj (vec unq))]
    
    (map #(reduce simplify (clojure.string/split % #"")) tc)
  
    ))


(solve (clojure.string/split ex #""))


