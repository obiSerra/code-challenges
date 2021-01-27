(ns advent2020.day4
 (:require [advent2020.utils :as utils]
           [clojure.string :as s]))

(def required [:byr :iyr :eyr :hgt :hcl :ecl :pid])

(defn dig4? [v]
  (= 4 (count v)))

(defn between? [v min max]
  (and (>= (Integer/parseInt v) min)
       (<= (Integer/parseInt v) max)))



(def params [[:byr #(and (dig4? %)
                         (between? % 1920 2002))]
             [:iyr #(and (dig4? %)
                         (between? % 2010 2020))]
             [:eyr #(and (dig4? %)
                         (between? % 2020 2030))]
             ]
)

(defn make-hash [data]
  (->> data
       (reduce (fn [acc val] 
                 (if (empty? val)
                   (conj acc [])
                   (conj (rest acc) (concat (first acc) 
                                            (map #(identity [(keyword (first %)) (last %)]) 
                                                 (map #(s/split % #":") (s/split val #" ")))))
                   )) [])
       (map (partial into {}))))

(defn solve [input]
  (count (filter true? (map (fn [coll] (every? #(contains? coll %) required)) (make-hash input)))))

(defn solve-gold [input]
  (make-hash input)
  )



(comment 

  (clojure.pprint/pprint (make-hash (utils/get-input 4 true)))
  (solve (utils/get-input 4))

  


  (map   
   (fn [h] (every? true? (map #((last %) (h (first %))) params)))
   (make-hash (utils/get-input 4 true)))



  )
