(ns advent2018.day6
  (:require [advent2018.utils :as utils]
            [clojure.string :as string]))

(def ex ["1, 1"
         "1, 6"
         "8, 9"
         "3, 4"
         "5, 5"
         "8, 3"])


(defn strs->points [strs]
  (map (comp
        #(map read-string %)
        #(string/split (string/replace % #" " "") #",") )
       strs))

(defn sort-points [strs]
  (sort-by #(read-string (str (first %) "." (last %))) strs))

(defn take-vert ([acc] acc)
  ([acc v] [(conj (first acc)
                  (first v))
            (conj (last acc)
                  (last v))]))

(defn verts [sorted] (reduce take-vert [[] []] sorted))

(defn edges [verts] [(set [(apply min (first verts))
                      (apply max (first verts))])

                (set [(apply min (last verts))
                      (apply max (last verts))])])


(defn not-infinite [edges sorted] (filter #(and
                                (nil? ((first edges) (first %)))
                                (nil? ((last edges) (last %)))) sorted))


(defn calc-dist [p1 p2]
  (+ (Math/abs (- (first p1) (first p2)))
     (Math/abs (- (last p1) (last p2)))))


(defn find-closest ([acc] acc)
  ([acc v] 
   (cond 
             (= 0 (:d v)) acc
             (or (nil? (:d acc)) 
                 (< (:d v) (:d acc))) (-> acc 
                                          (update-in [:d] (fn [_] (:d v)))
                                          (update-in [:pts] (fn [_] [(:p v)])))
             (= (:d v) (:d acc)) (update-in acc [:pts] (fn [old] (conj old (:p v))))
             :else acc)))

(defn closest [pt pts]
  (transduce (map #(hash-map :p % :d (calc-dist pt %)) )
             find-closest
             {:d nil :pts []}
             pts))

(comment 
  (closest (-> ex strs->points first) (-> ex strs->points))
)
